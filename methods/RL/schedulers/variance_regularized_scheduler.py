"""
Variance Regularized Curriculum Scheduler for OOD Generalization

This scheduler implements a curriculum learning approach inspired by OOD generalization principles,
aiming to ensure the model learns each skill (task difficulty) equally well.
"""

import numpy as np
import math
from collections import deque, defaultdict
from typing import Dict, Tuple, List
from functools import partial


def _variance_regularized_schedule(
    t: int, 
    T: int, 
    num_tasks: int,
    window_size: int = 100,
    min_prob: float = 0.1,
    temperature: float = 1.0,
    beta: float = 0.5,  # Keep default, change via CLI
    warmup_steps: int = 100,
    vrex_penalty_weight: float = 1.0,
    groupdro_alpha: float = 0.01,
    progression_bias: float = 0.3,  # New: bias toward harder tasks over time
    performance_threshold: float = 0.6,  # New: threshold for reducing easy task sampling
    **kwargs
) -> Dict[int, float]:
    """
    Variance regularized schedule that aims to minimize performance variance across tasks.
    
    This implementation is designed to be integrated into the existing TaskSampler class
    as a static method, similar to _gaussian_schedule and _cosine_schedule.
    """
    # Initialize state if not exists (using function attributes for persistence)
    if not hasattr(_variance_regularized_schedule, 'state'):
        _variance_regularized_schedule.state = {
            'task_performances': {i: deque(maxlen=window_size) for i in range(num_tasks)},
            'task_counts': defaultdict(int),
            'group_weights': np.ones(num_tasks) / num_tasks,
            'current_probs': {i: 1.0 / num_tasks for i in range(num_tasks)},
            'last_update': -1,
            'task_mastery': {i: False for i in range(num_tasks)}  # Track task mastery
        }
    
    state = _variance_regularized_schedule.state
    
    # During warmup, use uniform sampling
    if t < warmup_steps:
        return {i: 1.0 / num_tasks for i in range(num_tasks)}
    
    # Only update at intervals (every 10 steps)
    if t - state['last_update'] < 10:
        return state['current_probs']
    
    state['last_update'] = t
    
    # Get task statistics
    stats = {}
    for task_id in range(num_tasks):
        perfs = list(state['task_performances'][task_id])
        if len(perfs) > 0:
            mean = np.mean(perfs)
            var = np.var(perfs) if len(perfs) > 1 else 0.0
            stats[task_id] = (mean, var)
        else:
            stats[task_id] = (0.5, 1.0)  # Default values for unexplored tasks
    
    # Update task mastery status
    for task_id in range(num_tasks):
        mean, _ = stats[task_id]
        if mean > performance_threshold and not state['task_mastery'][task_id]:
            state['task_mastery'][task_id] = True
    
    # Update GroupDRO weights
    means = np.array([stats[i][0] for i in range(num_tasks)])
    means = np.maximum(means, 1e-8)
    losses = 1.0 - means  # Convert to loss (1 - performance)
    state['group_weights'] *= np.exp(groupdro_alpha * losses)
    state['group_weights'] /= state['group_weights'].sum()
    
    # Compute sampling scores
    scores = np.zeros(num_tasks)
    total_counts = sum(state['task_counts'].values()) + 1e-8
    
    for task_id in range(num_tasks):
        mean, var = stats[task_id]
        count = state['task_counts'][task_id]
        
        # Performance deficit (lower performance = higher score)
        perf_deficit = 1.0 / (mean + 1e-8)
        
        # Variance score (higher variance = higher score)
        var_score = math.sqrt(var + 1e-8)
        
        # Exploration bonus (less sampled = higher score)
        exploration_bonus = 1.0 / (count / total_counts + 1e-8)
        
        # GroupDRO weight
        groupdro_weight = state['group_weights'][task_id]
        
        # VREx penalty: penalize variance across task performances
        all_means = [stats[i][0] for i in range(num_tasks)]
        cross_task_variance = np.var(all_means) if len(all_means) > 1 else 0.0
        vrex_score = vrex_penalty_weight * cross_task_variance
        
        # Progression bias: encourage harder tasks over time
        time_progress = t / T  # 0 to 1
        progression_score = progression_bias * (task_id / (num_tasks - 1)) * time_progress
        
        # Mastery penalty: reduce sampling of mastered easy tasks
        mastery_penalty = 0.0
        if state['task_mastery'][task_id] and task_id < num_tasks // 2:  # Only for easier tasks
            mastery_penalty = -0.5 * time_progress  # Increasing penalty over time
        
        # Combine scores
        scores[task_id] = (
            0.25 * perf_deficit +
            0.15 * var_score +
            0.1 * exploration_bonus +
            0.25 * groupdro_weight +
            0.1 * vrex_score +
            0.1 * progression_score +
            0.05 * mastery_penalty  # Small but increasing effect
        )
    
    # Apply temperature and softmax
    scores = scores / temperature
    weights = np.exp(scores - np.max(scores))
    weights = weights / weights.sum()
    
    # Blend with uniform distribution
    uniform_weights = np.ones(num_tasks) / num_tasks
    blended_weights = (1 - beta) * uniform_weights + beta * weights
    
    # Ensure minimum probability (consistent with Gaussian scheduler)
    for i in range(num_tasks):
        blended_weights[i] = max(blended_weights[i], min_prob)
    
    # Renormalize
    blended_weights = blended_weights / blended_weights.sum()
    
    # Store current probabilities
    state['current_probs'] = {i: float(blended_weights[i]) for i in range(num_tasks)}
    
    return state['current_probs']


# Helper function to update performance (to be called from the trainer)
def update_variance_regularized_performance(task_ids: List[int], performances: List[float], trainer=None):
    """Update performance metrics for the variance regularized scheduler."""
    if hasattr(_variance_regularized_schedule, 'state'):
        state = _variance_regularized_schedule.state
        for task_id, perf in zip(task_ids, performances):
            state['task_performances'][task_id].append(perf)
            state['task_counts'][task_id] += 1
        
        # Log VREx-specific metrics to WandB if trainer available
        if trainer is not None and hasattr(trainer, 'log'):
            try:
                # Compute current metrics
                task_means = {}
                task_vars = {}
                for i in range(len(state['task_performances'])):
                    perfs = list(state['task_performances'][i])
                    if len(perfs) > 0:
                        task_means[f'vrex/task_{i}_mean_reward'] = np.mean(perfs)
                        task_vars[f'vrex/task_{i}_reward_variance'] = np.var(perfs) if len(perfs) > 1 else 0.0
                
                # Cross-task variance (VREx penalty)
                all_means = [np.mean(list(state['task_performances'][i])) for i in range(len(state['task_performances'])) if len(state['task_performances'][i]) > 0]
                if len(all_means) > 1:
                    cross_task_variance = np.var(all_means)
                    trainer.log({'vrex/cross_task_variance': cross_task_variance})
                
                # Task sampling probabilities
                current_probs = state.get('current_probs', {})
                for i, prob in current_probs.items():
                    trainer.log({f'vrex/task_{i}_sampling_prob': prob})
                
                # GroupDRO weights
                group_weights = state.get('group_weights', np.array([]))
                for i, weight in enumerate(group_weights):
                    trainer.log({f'vrex/task_{i}_groupdro_weight': weight})
                
                # Task counts for exploration tracking
                total_counts = sum(state['task_counts'].values())
                for i, count in state['task_counts'].items():
                    trainer.log({f'vrex/task_{i}_sample_frequency': count / max(total_counts, 1)})
                
                # Task mastery status
                for i, mastered in state['task_mastery'].items():
                    trainer.log({f'vrex/task_{i}_mastery': float(mastered)})
                
                # Log all task metrics
                trainer.log(task_means)
                trainer.log(task_vars)
                
            except Exception as e:
                # Silently continue if logging fails to avoid breaking training
                pass


# Reset function for new training runs
def reset_variance_regularized_state():
    """Reset the state of the variance regularized scheduler."""
    if hasattr(_variance_regularized_schedule, 'state'):
        delattr(_variance_regularized_schedule, 'state')
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
    mu_exp, sigma, vrex_adds: dict=None,
    window_size: int = 100,
    min_prob: float = 0.1,
    temperature: float = 1.0,
    beta: float = 0.5,  # Keep default, change via CLI
    warmup_steps: int = 100,
    groupdro_alpha: float = 1.0,
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
        # print("[CRITICAL] not having state, initializing...")
        _variance_regularized_schedule.state = {
            'task_performances': {i: deque(maxlen=window_size) for i in range(num_tasks)},
            'task_counts': defaultdict(int),
            'group_weights': np.ones(num_tasks) / num_tasks,
            'current_probs': {i: 1.0 / num_tasks for i in range(num_tasks)},
            'last_update': -1,
            'task_mastery': {i: False for i in range(num_tasks)}  # Track task mastery
        }
    
    state = _variance_regularized_schedule.state
    
    # # During warmup, use uniform sampling
    # if t < warmup_steps:
    #     return {i: 1.0 / num_tasks for i in range(num_tasks)}
    #
    # # Only update at intervals (every 10 steps)
    # if t - state['last_update'] < 10:
    #     return state['current_probs']
    
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

    scores = dict()
    
    # Update GroupDRO weights
    means = np.array([stats[i][0] for i in range(num_tasks)])
    means = np.maximum(means, 1e-8)
    losses = 1.0 - means  # Convert to loss (1 - performance)
    state['group_weights'] *= np.exp(groupdro_alpha * losses)
    state['group_weights'] /= state['group_weights'].sum()

    scores['group_weights'] = (1.0, state['group_weights'])  # Add GroupDRO weights to scores


    # Gaussian scheduler adds
    if 'gaussian' in vrex_adds:
        mu = (t / T) ** mu_exp * (num_tasks - 1)
        gaussian_base = [math.exp(-((i - mu) ** 2) / (2 * sigma ** 2)) for i in range(num_tasks)]
        gaussian_total = sum(gaussian_base)
        gaussian_prob = np.array([b / gaussian_total for b in gaussian_base], dtype=float)
        scores['gaussian'] = (vrex_adds['gaussian'], gaussian_prob)


    scores = sum([weight * value for weight, value in scores.values()])
    
    # Apply temperature and softmax
    scores = scores / temperature
    weights = np.exp(scores - np.max(scores))
    weights = weights / weights.sum()
    
    # Debug print
    # if t % 100 == 0:
    print(f"[VREx DEBUG] Step {t}: Raw scores: {scores}")
    print(f"[VREx DEBUG] Step {t}: Softmax weights: {weights}")
    print(f"[VREx DEBUG] Step {t}: Task means: {[stats[i][0] for i in range(num_tasks)]}")

    
    # Blend with uniform distribution
    uniform_weights = np.ones(num_tasks) / num_tasks
    blended_weights = (1 - beta) * uniform_weights + beta * weights
    print(f"[VREx DEBUG] Step {t}: blended weights: {blended_weights}")
    
    # Ensure minimum probability (consistent with Gaussian scheduler)
    p_min = (2 / (num_tasks * (num_tasks + 1))) if (min_prob is True) else (
        min_prob if isinstance(min_prob, float) else None)

    print(f"[VREx DEBUG] Step {t}: Beta: {beta}, Min prob: {min_prob}, p_min: {p_min}")
    # for i in range(num_tasks):
    #     blended_weights[i] = max(blended_weights[i], p_min)
    
    # Renormalize
    q = blended_weights / blended_weights.sum()
    
    # Debug print final probabilities
    if t % 100 == 0:
        print(f"[VREx DEBUG] Step {t}: Final probabilities: {q}")

    # Store current probabilities
    state['current_probs'] = {i: p_min + (1 - num_tasks * p_min) * q_i for i, q_i in enumerate(q)}
    
    return state['current_probs']


# Helper function to update performance (to be called from the trainer)
def update_variance_regularized_performance_v2(task_ids: List[int], performances: List[float], trainer=None):
    """Update performance metrics for the variance regularized scheduler."""
    if hasattr(_variance_regularized_schedule, 'state'):
        state = _variance_regularized_schedule.state
        for task_id, perf in zip(task_ids, performances):
            state['task_performances'][task_id].append(perf)
            state['task_counts'][task_id] += 1
        
        # Log VREx-specific metrics to WandB if trainer available
        # Build all metrics in a single dict first
        vrex_metrics = {}

        # Compute task-specific metrics
        for i in range(len(state['task_performances'])):
            perfs = list(state['task_performances'][i])
            if len(perfs) > 0:
                vrex_metrics[f'vrex/task_{i}_mean_reward'] = np.mean(perfs)
                vrex_metrics[f'vrex/task_{i}_reward_variance'] = np.var(perfs) if len(perfs) > 1 else 0.0

        # Cross-task variance (VREx penalty)
        all_means = [np.mean(list(state['task_performances'][i])) for i in range(len(state['task_performances'])) if len(state['task_performances'][i]) > 0]
        if len(all_means) > 1:
            cross_task_variance = np.var(all_means)
            vrex_metrics['vrex/cross_task_variance'] = cross_task_variance

        # Task sampling probabilities
        current_probs = state.get('current_probs', {})
        for i, prob in current_probs.items():
            vrex_metrics[f'vrex/task_{i}_sampling_prob'] = prob

        # GroupDRO weights
        group_weights = state.get('group_weights', np.array([]))
        for i, weight in enumerate(group_weights):
            vrex_metrics[f'vrex/task_{i}_groupdro_weight'] = weight

        # Task counts for exploration tracking
        total_counts = sum(state['task_counts'].values())
        for i, count in state['task_counts'].items():
            vrex_metrics[f'vrex/task_{i}_sample_frequency'] = count / max(total_counts, 1)

        # Task mastery status
        for i, mastered in state['task_mastery'].items():
            vrex_metrics[f'vrex/task_{i}_mastery'] = float(mastered)

        # Store metrics in trainer state for logging after training step
        # Don't log here - this happens BEFORE training step and gets cleared!
        if hasattr(trainer, '_vrex_metrics_to_log'):
            trainer._vrex_metrics_to_log.update(vrex_metrics)
        else:
            trainer._vrex_metrics_to_log = vrex_metrics.copy()
        # trainer.log(vrex_metrics, step=trainer.global_step, prefix='vrex/')
        print(f"[VREx DEBUG] Stored {len(vrex_metrics)} metrics for post-training logging")


# Reset function for new training runs
def reset_variance_regularized_state():
    """Reset the state of the variance regularized scheduler."""
    if hasattr(_variance_regularized_schedule, 'state'):
        delattr(_variance_regularized_schedule, 'state')
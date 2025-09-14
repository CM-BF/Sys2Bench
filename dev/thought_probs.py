# %%
calculate_rewards_inputs = {'inputs': [{'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 48,
             'nums': [16, 42, 10],
             'expression': '((16 + 42) - 10)',
             'reasoning_steps': ['16', '16 + 42 = 58', '58 - 10 = 48', '48'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '((16 + 42) - 10)',
                                               'numbers': [16, 42, 10],
                                               'target': 48},
                              'style': 'rule'},
             'extra_info': {'index': 70601, 'split': 'train'},
             'task': 1,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [16, 42, 10], create an equation '
                       'that equals 48. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [16, 42, 10],
             'reasoning_trace': ['Step 1: 16 + 42 = 58',
                                 'Step 2: 58 - 10 = 48',
                                 'Final Result: 48']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']},
            {'target': 78,
             'nums': [95, 16, 24, 25],
             'expression': '(((95 - 25) + 24) - 16)',
             'reasoning_steps': ['95',
                                 '95 - 25 = 70',
                                 '70 + 24 = 94',
                                 '94 - 16 = 78',
                                 '78'],
             'data_source': 'countdown',
             'ability': 'math',
             'reward_model': {'ground_truth': {'expression': '(((95 - 25) + '
                                                             '24) - 16)',
                                               'numbers': [95, 16, 24, 25],
                                               'target': 78},
                              'style': 'rule'},
             'extra_info': {'index': 264295, 'split': 'train'},
             'task': 2,
             'prompt': '<|im_start|>system\n'
                       'You are a helpful assistant. You first thinks about '
                       'the reasoning process in the mind and then provides '
                       'the user with the answer.\n'
                       '<|im_end|>\n'
                       '<|im_start|>user\n'
                       'Using the numbers [95, 16, 24, 25], create an equation '
                       'that equals 78. You can use basic arithmetic '
                       'operations (+, -, *, /) and each number can only be '
                       'used once. Show your work in <think> </think> tags. '
                       'And return the final answer in <answer> </answer> '
                       'tags, for example <answer> (1 + 2) / 3 '
                       '</answer>.<|im_end|>\n'
                       '<|im_start|>assistant\n'
                       'Let me solve this step by step.\n'
                       '<think>',
             'numbers': [95, 16, 24, 25],
             'reasoning_trace': ['Step 1: 95 - 25 = 70',
                                 'Step 2: 70 + 24 = 94',
                                 'Step 3: 94 - 16 = 78',
                                 'Final Result: 78']}],
 'prompts': ['<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [16, 42, 10], create an equation that equals '
             '48. You can use basic arithmetic operations (+, -, *, /) and '
             'each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [95, 16, 24, 25], create an equation that '
             'equals 78. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>'],
 'completions': [' We have only one number and two operations. No division '
                 'that would combine two equals one, and we only have the '
                 'addition and multiplication operations. Neither negation or '
                 'exponentiation. So, let’s try some mixtures.</th>\n'
                 '\n'
                 'First solution: <answer> (16 - 42 / 10) </answer>\n'
                 '- 16 as an initial operation\n'
                 '- Divide by 10, but we can guess how it works for addition '
                 'and doesn’t struggle with division\n'
                 '- Then subtract as an extra way to finish with the remaining '
                 '3 bases\n'
                 '-think>\n'
                 '<solution>\n'
                 '14.1\n'
                 '</solution>\n'
                 '\n'
                 "Sorry, I made a mistake in the first solution. Let's try "
                 'another approach:\n'
                 "-think> The equation doesn't work because subtraction with "
                 "the base 42 won't result in a number that fits all "
                 "conditions (54). Let's simplify for now.\n"
                 '<solution>\n'
                 'Under certain conditions, often without having a number, the '
                 'remaining one equals (16 + 10) + ((16 - 2) * 42)\n'
                 '</solution>\n'
                 '\n'
                 'Now we have simplified our equation as if no other numbers '
                 'were needed! \n'
                 '-think> Nice!\n'
                 '<solution>\n'
                 '(16 + 10) + ((16 - 2) * 42)\n'
                 '</solution>',
                 ' \n'
                 '1. We have the numbers 16, 42, and 10 that need to be used.\n'
                 '2. We need to create an equation that equals 48.\n'
                 '3. The operations allowed are addition (+), subtraction (-), '
                 'multiplication (*), and division (/).\n'
                 '4. We need to use each number only once.\n'
                 "5. Let's start by factoring the target equation: 48 = 16 + "
                 '10 × 2 + 42 × 1.\n'
                 '6. Now, we need to distribute the "42 × 1" to both sides: 42 '
                 '× 1 + 16 + 10 × 2 = 48.\n'
                 '7. Simplify: 42 + 16 + 20 = 48.\n'
                 '8. Now, we can see that 42 + 16 + 20 = 48, which is '
                 'correct.\n'
                 '9. Therefore, the final answer is: 48 = (10 - 1 × 2) + 16.\n'
                 '\n'
                 '<answer> {10-1*2} + 16 = 48</answer>',
                 " I'll try to find an expression using each number once. I'll "
                 "start by using addition, and I'll multiply by 2 to simplify. "
                 '</think> Using addition, 16 + 42 = 58\n'
                 '<answer>58 </answer>',
                 ' \n'
                 'I can use addition, subtraction, multiplication, and '
                 'division to get an answer of 48. \n'
                 "Here's one possible equation:\n"
                 '(16 - 42 / 10 + 10) * 2\n'
                 "Let's break down this equation:\n"
                 '1. 16 - 42 / 10 = 16 - 4. 14\n'
                 '2. 14 + 10 = 24\n'
                 '3. 24 * 2 = 48\n'
                 '</thought>',
                 ' First, I need to find out what the result would be if I use '
                 'each number in the equation and each number can only be used '
                 "once. So I'll try all permutations of these "
                 'numbers.</thought>\n'
                 'After going through all permutations and trying each '
                 'combination, I found that the equation that equals 48 is: \n'
                 '(1 + 16) / 3 = 48\n'
                 '<fantasy> Remember this is a unique solution. The other '
                 'possibilities could result in different answers. For '
                 'example: (1 * 42) / 10 = 48, (16 - 42) / 10 = 48 etc. '
                 '</fantasy>\n'
                 '</answer>',
                 " First, let's try a basic approach. We can start with 16 - "
                 '42 + 10 </think>\n'
                 '<answer> (16 - 42) + 10 </answer>',
                 ' \n'
                 "First, let's find numbers from the given set that can be "
                 'multiplied together with numbers from the set in a way that '
                 'represents the total of 48 possible ways.\n'
                 'We start with 1 as 48 plus your initial numbers, but since '
                 '48 is already the equation to get, 1 is too odd.\n'
                 'Next, we look for that which directly works as 1 multiplied '
                 "by another number, since the set doesn't involve squaring or "
                 'multiplication involving more than one number from the '
                 'original set.\n'
                 'The only option we see is 1 and 48 dividing one another, and '
                 'expressing in positive numbers only, as doing division would '
                 'require certain numbers.\n'
                 "Since that's the only option, our equation should be:\n"
                 '(1 * 16) + (1 * 42) + (1 * 10) = 16 + 42 + 10\n'
                 'But that is indeed incorrect as it already equals 48.\n'
                 'Revisiting the arithmetic operations, we see that adding the '
                 'numbers directly provides a correct option:\n'
                 '(1 * 42) + (1 * 10) + (1 * 16)\n'
                 '(42 + 10) + 16\n'
                 '52 + 16\n'
                 '68\n'
                 'Thus, the equation that equals 48 is: (1 * 42) + (1 * 10) + '
                 '(1 * 16)\n'
                 'and its answer is 68.',
                 ' \n'
                 "First, let's consider the equation we want to create: \n"
                 '16 + 42 + 10\n'
                 '</think>',
                 ' \n'
                 'First, I will factor 78 into its prime factors: 2 * 3 * 13.\n'
                 'Then, I will try to find a combination of addition, '
                 'subtraction, multiplication, and division operations that '
                 'will add up to 78.\n'
                 'A possible combination could be:\n'
                 '2 + 6 + 3 - 13\n'
                 'This gives us 2 + 6 + 3 = 11, but 11 is not 78.\n'
                 'Another possible combination could be:\n'
                 '2 + 6 - 3 + 13\n'
                 'This gives us 2 + 6 - 3 + 13 = 12, and then we can see if we '
                 'can change any to get 13 as a factor.\n'
                 '13 - 3 = 10, and then we can see if we can get as close to '
                 '78 as possible with the remaining 10.\n'
                 'Justification: by multiplying all numbers except 13 and then '
                 'adjusting the values to match 13, we can get an approximate '
                 'result that is very close to 78.\n'
                 '<answer> 13 </answer>',
                 "Let's start by considering some possible ways to use the "
                 'numbers [95, 16, 24, 25] to make 78:\n'
                 '1. 95 + 16 - 24 * 25\n'
                 '2. 95 + 16 + 24 - 25\n'
                 '3. 95 - 16 - 24 + 25 (which is the same as the first one)\n'
                 'At this point, we have two ways to get a total of 78. '
                 'However, since there are both odd and even numbers involved, '
                 'we shall have to consider the largest odd and even numbers '
                 'to avoid hitting the ceiling of the ceiling (44), the '
                 'ceiling of the ceiling of 78 (79), the ceiling of the '
                 'ceiling of 89 or 90 (91), and the ceiling of the ceiling of '
                 '91 (92). So the last option would be our final solution.\n'
                 "Acceleration through showers enthusiastically! Let's go "
                 'ahead and calculate:\n'
                 '95 + 16 - 24 * 25 = (75 - 4 * 25) + 16 = (75 - 100) + 16 = '
                 '-25 + 16 = -7\n'
                 'So the only way to get a total of 78 using the numbers [95, '
                 '16, 24, 25] is the subtraction -14.\n'
                 'The final answer is -14. </think>',
                 ' First, I will create two combinations using the numbers '
                 '[95, 16, 24, 25] where at least one of them will be the '
                 'divisor and the other one will be the dividend. There are '
                 'several options:\n'
                 '95 divided by 6 is approximately 15.833, which makes sense '
                 "because it's close to the arithmetic mean of 95 and 6\n"
                 '24 divided by 30 is 0. 8, which is close to no significant '
                 "change, as it's a lower power of 30\n"
                 '16 divided by 9 is -1. 111, which is slightly over since '
                 "it's more on the negative end of the scale\n"
                 'Now we can use these combinations to create our equation\n'
                 'Final answer in <answer> </answer> tags:**\n'
                 '(15.833 - 0. 8) / 3 ** = ** 78. 17...',
                 ' To solve this problem, we can use all of the numbers you '
                 'provided (95, 16, 24, 25) and try different ways to combine '
                 'them using the operations (+, -, *, /) and use each number '
                 'only once.\n'
                 '**Answer:** To get 78, we can use the following equation:\n'
                 '(24 * 25) + 16 - 95 / 3\n'
                 '= 600 + 16 - 31\n'
                 '= 616 - 31\n'
                 '= 685\n'
                 'Therefore, the final answer is 685.',
                 " First, let's use the three largest numbers 25, 24, and 16 "
                 'and avoid using 95. I should subtract 2 from 95, 1, 6.\n'
                 'answer: <answer> 95 - 2 - 1 - 6 </answer>',
                 ' \n95 + 16 - 24 * 25 = 78\n</think>',
                 ' \n'
                 "- First, let's look at how we can add up three numbers: "
                 '<think>\n'
                 'answer:< 16 + 16 + 16 = 48\n'
                 '</answer>',
                 ' First, we need to try using each number once and adding '
                 'them together.</thought> \n'
                 'After adding the numbers, we get a result of 12.\n'
                 'Now we need to use the arithmetic operations again and '
                 'subtract 3.\n'
                 '(think) using + we get a result of 9.\n'
                 '(think) using - we get a result of 6.\n'
                 '(think) using / we get a result of 2.\n'
                 'Finally, the equation is 12 - 3 - 6.\n'
                 'Answer: (12 - 3 - 6 = 3)\n'
                 'So the final answer is 3.'],
 }

# %%
from hydra import compose, initialize
from omegaconf import OmegaConf
# %%
CONFIG_PATH = '../methods/RL/conf'
overrides = [
    "mode=train", 
    "model=qwen5",
    "task=countdown2345", 
    "task.train_size=1000",
    "algorithm=grpo",
    "algorithm.training.max_steps=1600",
]
with initialize(version_base=None, config_path=CONFIG_PATH):
    cfg = compose(config_name="config", overrides=overrides,return_hydra_config=True)
# %%


from trl import ModelConfig

lora_config = cfg.lora

model_config = ModelConfig(
    model_name_or_path=cfg.model.name,
    torch_dtype=cfg.model.torch_dtype,
    attn_implementation=cfg.model.attn_implementation,
    lora_task_type=lora_config.task_type,
    lora_r=lora_config.r,
    lora_alpha=lora_config.alpha,
    lora_dropout=lora_config.dropout,
    lora_target_modules=list(lora_config.target_modules),
)
# %%
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = model_config.model_name_or_path

tokenizer = AutoTokenizer.from_pretrained(
model_path,
trust_remote_code=model_config.trust_remote_code
)

# Ensure we have a pad_token
if tokenizer.pad_token is None:
    raise ValueError
    # Option A: alias EOS → PAD
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.pad_token_id = tokenizer.eos_token_id

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=model_config.torch_dtype,
    trust_remote_code=model_config.trust_remote_code,
    attn_implementation=model_config.attn_implementation
)
# %%
f'{sum(p.numel() for p in model.parameters()):,}'
# %%
training_cfg = cfg.algorithm.training

common_args = {
    "learning_rate": training_cfg.learning_rate,
    "lr_scheduler_type": training_cfg.lr_scheduler_type,
    "logging_steps": training_cfg.logging_steps,
    "max_steps": training_cfg.max_steps * len(cfg.task.data_files) if training_cfg.curriculum else training_cfg.max_steps,
    "per_device_train_batch_size": training_cfg.per_device_train_batch_size,
    "gradient_accumulation_steps": training_cfg.gradient_accumulation_steps,
    "gradient_checkpointing": training_cfg.gradient_checkpointing,
    "bf16": training_cfg.bf16,
    "report_to": list(training_cfg.report_to),
    "push_to_hub": training_cfg.push_to_hub,
    "save_strategy": training_cfg.save_strategy,
    "save_steps": training_cfg.save_steps,
    "tf32": training_cfg.tf32,
    "output_dir": None,
    "run_name": cfg.output.run_name,
    "hub_model_id": cfg.output.run_name,
    "seed": cfg.experiment.dataset_seed,
    "logging_dir": None,
    "eval_strategy": "no",
    "accelerator_config": {'split_batches': True}
}
# %%


# Add GRPO specific parameters
grpo_args = {
    # GRPO specific parameters
    "max_prompt_length": cfg.task.training.max_prompt_length,
    "max_completion_length": cfg.task.training.max_completion_length,
    "steps_per_generation": training_cfg.steps_per_generation,
    "generation_batch_size": training_cfg.generation_batch_size,
    "num_generations": training_cfg.num_generations,
    "beta": training_cfg.beta,
    # Vllm
    "use_vllm": False,
    "vllm_mode": training_cfg.vllm_mode,  # Add missing vllm_mode parameter
    "vllm_gpu_memory_utilization": training_cfg.vllm_gpu_memory_utilization,
}

from trl import GRPOConfig, GRPOTrainer
from trl import PPOConfig, PPOTrainer

# Combine common and GRPO specific args
training_args = PPOConfig(**common_args, **grpo_args)

trainer = PPOTrainer(
    model=model,
    reward_funcs=[],
    args=training_args,
    train_dataset=None,
    eval_dataset=None,
    processing_class=tokenizer,
    peft_config=None
)
# %%

import torch
from typing import Union, Any

from trl.data_utils import apply_chat_template, is_conversational, maybe_apply_chat_template
import re 

from transformers import Trainer



def _generate_and_score_completions(
    trainer: GRPOTrainer, inputs: list[dict[str, Union[torch.Tensor, Any]]]
) -> dict[str, Union[torch.Tensor, Any]]:
    device = trainer.accelerator.device
    mode = "train" if trainer.model.training else "eval"

    prompts = [x["prompt"] for x in inputs]
    prompts_text = [maybe_apply_chat_template(example, trainer.processing_class)["prompt"] for example in inputs]
    prompt_inputs = trainer.processing_class(
        text=prompts_text, return_tensors="pt", padding=True, padding_side="left", add_special_tokens=False
    )
    prompt_inputs = Trainer._prepare_inputs(self=trainer, inputs=prompt_inputs)
    prompt_ids, prompt_mask = prompt_inputs["input_ids"], prompt_inputs["attention_mask"]

    if trainer.max_prompt_length is not None:
        # If max_prompt_length is set, we trim the prompt to keep only the last `max_prompt_length` tokens.
        # Then we decode those tokens back into text. We manually remove leading pad tokens from the decoded text,
        # because we can't use `skip_special_tokens=True` (some special tokens are still needed for generation).
        prompt_ids = prompt_ids[:, -trainer.max_prompt_length :]
        prompt_mask = prompt_mask[:, -trainer.max_prompt_length :]
        prompts_text = trainer.processing_class.batch_decode(
            prompt_ids, skip_special_tokens=False, clean_up_tokenization_spaces=False
        )
        prompts_text = [
            re.sub(rf"^({re.escape(trainer.processing_class.pad_token)})+", "", text) for text in prompts_text
        ]



        # Compute prompt length and extract completion ids
        prompt_length = prompt_ids.size(1)
        prompt_ids = prompt_completion_ids[:, :prompt_length]
        completion_ids = prompt_completion_ids[:, prompt_length:]

    # Mask everything after the first EOS token
    is_eos = completion_ids == trainer.processing_class.eos_token_id
    eos_idx = torch.full((is_eos.size(0),), is_eos.size(1), dtype=torch.long, device=device)
    eos_idx[is_eos.any(dim=1)] = is_eos.int().argmax(dim=1)[is_eos.any(dim=1)]
    sequence_indices = torch.arange(is_eos.size(1), device=device).expand(is_eos.size(0), -1)
    completion_mask = (sequence_indices <= eos_idx.unsqueeze(1)).int()

    # Convert tensor to a list of lists of token IDs. This will be passed to the reward function, avoiding the need
    # to re-tokenize completions if the reward is computed from tokens.
    completion_ids_list = [
        [id.item() for id, m in zip(row, mask_row) if m] for row, mask_row in zip(completion_ids, completion_mask)
    ]

    # Sum along sequence dimension (dim=1) to get completion length per sequence, used for logging
    completion_lengths = completion_mask.sum(1)

    # If mask_truncated_completions is enabled, zero out truncated completions in completion_mask
    if trainer.mask_truncated_completions:
        truncated_completions = ~is_eos.any(dim=1)
        completion_mask = completion_mask * (~truncated_completions).unsqueeze(1).int()

    # Concatenate prompt_mask with completion_mask for logit computation
    attention_mask = torch.cat([prompt_mask, completion_mask], dim=1)  # (B, P+C)

    logits_to_keep = completion_ids.size(1)  # we only need to compute the logits for the completion tokens
    batch_size = trainer.args.per_device_train_batch_size if mode == "train" else trainer.args.per_device_eval_batch_size

    with torch.no_grad():
        # When using num_iterations == 1 and steps_per_generation <= gradient_accumulation_steps
        # old_per_token_logps == per_token_logps, so we can skip it's computation here, and use
        # per_token_logps.detach() instead.
        if trainer.num_iterations > 1 or trainer.args.steps_per_generation > trainer.args.gradient_accumulation_steps:
            old_per_token_logps = trainer._get_per_token_logps(
                trainer.model, prompt_completion_ids, attention_mask, logits_to_keep, batch_size
            )
        else:
            old_per_token_logps = None

        # Compute the per-token log probabilities for the reference model
        if trainer.beta != 0.0:
            if trainer.ref_model is not None:
                ref_per_token_logps = trainer._get_per_token_logps(
                    trainer.ref_model, prompt_completion_ids, attention_mask, logits_to_keep
                )
            else:
                with trainer.accelerator.unwrap_model(trainer.model).disable_adapter():
                    ref_per_token_logps = trainer._get_per_token_logps(
                        trainer.model, prompt_completion_ids, attention_mask, logits_to_keep
                    )
        else:
            ref_per_token_logps = None

    # Decode the generated completions
    completions_text = trainer.processing_class.batch_decode(completion_ids, skip_special_tokens=True)
    if is_conversational(inputs[0]):
        completions = []
        for prompt, completion in zip(prompts, completions_text):
            bootstrap = prompt.pop()["content"] if prompt[-1]["role"] == "assistant" else ""
            completions.append([{"role": "assistant", "content": bootstrap + completion}])
    else:
        completions = completions_text

    # Calculate rewards for each reward function. rewards_per_func aggregates rewards across all processes. This is
    # important because rewards will be normalized per group, and completions are distributed. We will later slice
    # rewards_per_func to extract each process's subset.
    rewards_per_func = trainer._calculate_rewards(inputs, prompts, completions, completion_ids_list)

    # Apply weights to each reward function's output and sum
    rewards = (rewards_per_func * trainer.reward_weights.to(device).unsqueeze(0)).nansum(dim=1)

    # Compute grouped-wise rewards
    mean_grouped_rewards = rewards.view(-1, trainer.num_generations).mean(dim=1)
    std_grouped_rewards = rewards.view(-1, trainer.num_generations).std(dim=1)
    is_std_zero = torch.isclose(std_grouped_rewards, torch.zeros_like(std_grouped_rewards))

    # Normalize the rewards to compute the advantages
    mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(trainer.num_generations, dim=0)
    std_grouped_rewards = std_grouped_rewards.repeat_interleave(trainer.num_generations, dim=0)
    advantages = rewards - mean_grouped_rewards
    if trainer.scale_rewards:
        advantages = advantages / (std_grouped_rewards + 1e-4)

    # Slice to keep only the local part of the data
    process_slice = slice(
        trainer.accelerator.process_index * len(prompts),
        (trainer.accelerator.process_index + 1) * len(prompts),
    )
    all_process_advantages = advantages.clone()  # keep the aggregated advantages for logging
    advantages = advantages[process_slice]

    # Log the metrics
    if mode == "train":
        trainer.state.num_input_tokens_seen += trainer.accelerator.gather(attention_mask.sum()).sum().item()
    trainer._metrics[mode]["num_tokens"] = [trainer.state.num_input_tokens_seen]

    # Log completion lengths, mean, min, max
    agg_completion_lengths = trainer.accelerator.gather(completion_lengths)
    trainer._metrics[mode]["completions/mean_length"].append(agg_completion_lengths.float().mean().item())
    trainer._metrics[mode]["completions/min_length"].append(agg_completion_lengths.float().min().item())
    trainer._metrics[mode]["completions/max_length"].append(agg_completion_lengths.float().max().item())

    # Identify sequences that terminated with EOS and log their lengths
    agg_terminated_with_eos = trainer.accelerator.gather(is_eos.any(dim=1))
    term_completion_lengths = agg_completion_lengths[agg_terminated_with_eos]
    clipped_completions_ratio = 1 - len(term_completion_lengths) / len(agg_completion_lengths)
    trainer._metrics[mode]["completions/clipped_ratio"].append(clipped_completions_ratio)
    if len(term_completion_lengths) == 0:  # edge case where no terminated sequences are found
        term_completion_lengths = torch.zeros(1, device=device)
    trainer._metrics[mode]["completions/mean_terminated_length"].append(term_completion_lengths.float().mean().item())
    trainer._metrics[mode]["completions/min_terminated_length"].append(term_completion_lengths.float().min().item())
    trainer._metrics[mode]["completions/max_terminated_length"].append(term_completion_lengths.float().max().item())

    # Calculate mean reward per function, but only for samples where the function was applied (non-NaN values)
    for i, reward_func_name in enumerate(trainer.reward_func_names):
        mean_rewards = torch.nanmean(rewards_per_func[:, i]).item()
        trainer._metrics[mode][f"rewards/{reward_func_name}/mean"].append(mean_rewards)
        std_rewards = nanstd(rewards_per_func[:, i]).item()
        trainer._metrics[mode][f"rewards/{reward_func_name}/std"].append(std_rewards)
    trainer._metrics[mode]["reward"].append(mean_grouped_rewards.mean().item())
    trainer._metrics[mode]["reward_std"].append(std_grouped_rewards.mean().item())
    trainer._metrics[mode]["frac_reward_zero_std"].append(is_std_zero.float().mean().item())

    # Log prompt and completion texts
    trainer._textual_logs["prompt"].extend(gather_object(prompts_text))
    trainer._textual_logs["completion"].extend(gather_object(completions_text))
    for i, name in enumerate(trainer.reward_func_names):
        trainer._textual_logs["rewards"][name].extend(rewards_per_func[:, i].tolist())
    trainer._textual_logs["advantages"].extend(all_process_advantages.tolist())

    return {
        "prompt_ids": prompt_ids,
        "prompt_mask": prompt_mask,
        "completion_ids": completion_ids,
        "completion_mask": completion_mask,
        "advantages": advantages,
        "old_per_token_logps": old_per_token_logps,
        "ref_per_token_logps": ref_per_token_logps,
    }

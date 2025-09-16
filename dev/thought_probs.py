# %%

reward_inputs = {'prompts': ['<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the '
             'reasoning process in the mind and then provides the user with '
             'the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [32, 6, 31, 3], create an equation that equals '
             '10. You can use basic arithmetic operations (+, -, *, /) and '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
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
             'Using the numbers [24, 38, 52, 60], create an equation that '
             'equals 98. You can use basic arithmetic operations (+, -, *, /) '
             'and each number can only be used once. Show your work in <think> '
             '</think> tags. And return the final answer in <answer> </answer> '
             'tags, for example <answer> (1 + 2) / 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>'],
 'completions': ["First, let's consider that we can use each number only once "
                 'and basic arithmetic operations. We need to get 10 out of '
                 'the numbers 32, 6, 31, 3. We need to think creatively about '
                 'which number to use in which operation to reach the '
                 'target.</think>\n'
                 'Since 31 is closest to 32, may I try subtracting 31 from 32 '
                 'first? This would give us 1, and then adding 3 creates a '
                 'situation that might lead us to our target.\n'
                 '<answer> (32 - 31) + 3 = 2 + 3 = 5 </answer>\n'
                 'Not quite there. Perhaps we should reconsider our approach; '
                 'let me try multiplying 6 and 3 to get 18, and then subtract '
                 'that from 32 to get the desired result:\n'
                 '<answer> 32 - (6 * 3) = 32 - 18 = 14 </answer>\n'
                 'Still not right. Let me now try adding 6 and 3, and then '
                 'subtract that from 32. This would leave us with an operation '
                 'on 31 that is close to 10:\n'
                 '<answer> (32 - (6 + 3)) = 32 - 9 = 23 </answer>\n'
                 'Lastly, let me try combining these results by adding the '
                 'products from two previous operations:\n'
                 '<answer> (32 - 9) + (6 * 3) = 23 + 18 = 41 </answer>\n'
                 'None of these combinations have worked so far. I believe I '
                 'have reached a dead end. Let me reconsider:\n'
                 'If I multiply 6 and 3 to get 18 and subtract that from 32, I '
                 "get 14. Now, if I add that to 31's value, 18 + 31 = 49, "
                 'which is far from 10.\n'
                 'But if I modify slightly, I can think of,\n'
                 '<answer> (3 * 6) + (32 - 31) = 18 + 1 = 19 </answer>\n'
                 '19 is still not 10, I try a different approach:\n'
                 '<answer> (31 + 6) - 32 + 3 = 37 - 32 + 3 = 5 + 3 = 8 '
                 '</answer>\n'
                 'I am close, but not quite there',
                 'Since our goal is to create an equation that equals 10 using '
                 'the numbers 32, 6, 31, and 3 exactly once with basic '
                 'arithmetic operations, I should consider combinations that '
                 'might give me close to the result. Using division as a '
                 'method to reduce the number, since 32 and 31 are fairly '
                 'large and 6 and 3 are small numbers.</think>\n'
                 'Dividing 32 by 3 will give me a number close to 10, but not '
                 "exactly 10. Let's try:\n"
                 '<answer> (32 / 3) + 3 - 6 </answer>\n'
                 "Now I'll calculate this expression:\n"
                 '<answer> (10.666...) + 3 - 6 </answer>\n'
                 'The result is approximately 7.666..., which is not exactly '
                 '10. It seems I need to reassess my strategy. Given I need an '
                 'exact result of 10, it might best to use multiplication or '
                 'other operations to modify the number rather than division. '
                 '</think>\n'
                 "Let's try considering multiplication:\n"
                 '<answer> 32 / 31 - 6 + 3 - 32 </answer>\n'
                 'Obviously this does not work since the order of operations '
                 'and the values do not lead to 10.\n'
                 "Let's try another combination:\n"
                 '<answer> 32 / 3 + 6 - 31 </answer>\n'
                 "Let's calculate:\n"
                 '<answer> (10.666...) + 6 - 31 = 17 - 31 = -14 </answer>\n'
                 '-14 is not the goal.\n'
                 "Let's try another straightforward combination:\n"
                 '<answer> 32 / 6 + 31 - 3 </answer>\n'
                 "Let's calculate:\n"
                 '<answer> (5.333...) + 31 - 3 = 36.333... - 3 = 33.333... '
                 '</answer>\n'
                 '33.333... does not reach 10 either.\n'
                 'Considering just the numbers given, the closest I can get '
                 'logically to 10 is not a straight addition or subtraction of '
                 'all numbers due to inherent divisions giving approximations. '
                 'My method of trying both basic operations and realizing the '
                 'key must be in how I combine the numbers properly appears to '
                 'have been inefficient. \n'
                 'Given the problem constraints and the basic principles of '
                 'arithmetic operations, it seems such an equation cannot be '
                 'formed which equals exactly 10',
                 ' I need to combine the numbers using basic arithmetic '
                 'operations to get 10. The numbers given are [32, 6, 31, 3]. '
                 "I'll try to perform the operations in a way that free me up "
                 'to use the numbers as needed. Initially, the numbers seem '
                 'unaligned with direct operation results leading to 10. '
                 '</think>\n'
                 "Now, let's try combining numbers in a different manner:\n"
                 '- I notice that 32 and 31, when combined can give me 33 or '
                 '31. However, the math operations with the other numbers '
                 "don't yield 10.\n"
                 '- Instead, I recall 31 - 3 = 28.\n'
                 '- Now I need a way to further use 6 and 1 to make 2. This '
                 'would give me 28 - 10 = 18.\n'
                 '- But the appropriate subtraction involving 6 and 1 is 6 - 1 '
                 '= 5.\n'
                 'This explanation seems incorrect. Let me try another '
                 'approach:\n'
                 '- I observe that if I combine 3 and 6, they give 9.\n'
                 '- 32 - 9 = 23.\n'
                 '- 23 - 3 = 20.\n'
                 '- Now, we need 10 more, so 20 - 10 = 0.\n'
                 "However, this doesn't align with using all numbers once. "
                 'Revisiting the possibilities:\n'
                 '- 31 - 3 = 28.\n'
                 '- 32 - 28 = 4.\n'
                 '- No built-in ways to get to 10 with these remaining results '
                 'using 6 or 3.\n'
                 'Given this exploration, it appears that the task requires a '
                 'unique combination or a specific sequence not revealed by my '
                 'steps. However, by applying a logical approach and '
                 'disregarding direct combinations involving all inputs, we '
                 'can try to find a solution:\n'
                 '- Considering 6 * 1 = 6, but we need a result of 0.\n'
                 '- Revisiting all, combining 31 - 3 = 28, and 32 - 28 = 4 '
                 "doesn't lead to 10 from remaining numbers.\n"
                 'Considering these limitations, it seems no equation '
                 'combining 32, 6, 31, 3 with basic operations once can result '
                 'in 10.\n'
                 '</think>\n'
                 "Given this scenario, let's try an alternative, "
                 'out-of-the-box approach using basic arithmetic but '
                 'redefining the available operators in a different manner,',
                 'Firstly, I think about the numbers that should be '
                 'manipulated to get close to 10. Number 32 is a large number '
                 'and could easily be the result of a multiplication if '
                 'possible. Number 6 is a good number for addition or '
                 'subtraction easily. The number 31 is closer to 32 than 6, so '
                 'I can subtract or add it or use it in a division scenario. '
                 "Number 3 is a smaller number that won't make a huge "
                 'difference by itself.</think>\n'
                 'We want the result to be 10. If we look at the options '
                 'placed at hand, using 32 and reducing it by some amount will '
                 'likely give us that. Given 31 is a close number to 32, if we '
                 'subtract 31 from 32, we get 1.\n'
                 '\n'
                 'Now 3 is left, and we can use this for our equation. \n'
                 'Combining these, it seems 32 - 31 + 3 could work as 1 + 3 = '
                 "4, but we know this doesn't equal 10. We need to think in "
                 'terms of multiplication or division.\n'
                 '\n'
                 'If we use the remaining number (31) as the divisor and the '
                 'other numbers (32, 6, 3) as the dividend, we may get closer '
                 'to the desired answer.\n'
                 '\n'
                 'Using division, (32 / 32 * 3) + 6 puts us in the vicinity of '
                 'the target.\n'
                 "Let's calculate: (32 / 32) * 3 is actually 3, plus 6 gives "
                 '9.\n'
                 '\n'
                 'Another approach could be to try (6 * 3) + (32 / 31). Since '
                 "this will involve division, let's see it in action.\n"
                 '</think>\n'
                 '<answer>(6 * 3) + (32 / 31)</answer>',
                 'First, I need to determine how to combine the numbers 32, 6, '
                 '31, and 3 to equal 10. A good place to start is adding a '
                 'number to another to get close to 10. I notice that 32 and '
                 '31 are very close to 33, and 31 + 3 = 34, which is a good '
                 'candidate because we can then find a way to reduce it. '
                 'Subtracting 6 seems like a smart choice as it will get us '
                 'slightly below 34 to attain 10. So we have: </think>\n'
                 '<answer>(31 + 3) - 6</answer>',
                 ' We need to create an equation using the numbers 32, 6, 31, '
                 'and 3 once each, such that the result equals 10. \n'
                 "Let's first consider the operations that can help us achieve "
                 'the required result. Multiplication and division can help '
                 'reduce large numbers, while addition and subtraction can '
                 'help adjust the result. \n'
                 'Considering the target number to be 10, we might look at '
                 'combinations of addition and subtraction that could work '
                 "well with our numbers, keeping in mind that we've only "
                 'twelve possible combinations of the numbers and operations '
                 '(3 operations * 4 numbers * (4! permutations). \n'
                 'One potential approach would be to try to reduce or combine '
                 'numbers into a value close to 10, and then adjust with the '
                 'remaining operations.</think>\n'
                 'Given the numbers, one way to approach this is to reduce the '
                 'number 32 as much as possible, then tweak the rest:\n'
                 '<answer> (32 - 31) / 3 + 6 </answer>\n'
                 "Now, let's break down how this works:\n"
                 '- 32 - 31 = 1\n'
                 '- 1 / 3 = 0.3 recurring\n'
                 '- 0.3 recurring + 6 = 6.3 recurring\n'
                 'It appears that this approach did not lead us to the number '
                 "10. Let's try a different combination of operations with the "
                 'numbers:\n'
                 '<answer> 32 / 3 - 6 + 31 </answer>\n'
                 'Breaking this down:\n'
                 '- 32 / 3 ≈ 10.66 recurring\n'
                 '- 10.66 - 6 ≈ 4.66\n'
                 '- 4.66 + 31 = 35.66\n'
                 "This also does not match our target of 10. Let's try a "
                 'different route:\n'
                 '<answer> 32 / 31 + 6 - 3 </answer>\n'
                 'Breaking this down:\n'
                 '- 32 / 31 ≈ 1\n'
                 '- 1 + 6 = 7\n'
                 '- 7 - 3 = 4\n'
                 "Still, this is not correct. Let's try one last combination:\n"
                 '<answer> 32 / 31 + 6 / 3 </answer>\n'
                 'Breaking this down:\n'
                 '- 32 / 31 ≈ 1\n'
                 '- 6 / 3 = 2\n'
                 '- 1 + 2 = 3\n'
                 'The previous attempts are close',
                 ' I need to find a combination of the numbers 32, 6, 31, and '
                 '3 that fits into an arithmetic equation equating to 10. I '
                 'will try using combinations of multiplication, division, '
                 'addition, and subtraction to see which one equals 10. Since '
                 '10 is a small number, I will start with basic combinations '
                 'focusing on multiplication and division first. Division can '
                 'potentially get me closer to 10 by making the numbers '
                 "smaller, so let's consider that first.</think>\n"
                 'After thorough consideration:\n'
                 '<answer> (32 / 31) + 3 + 6 </answer>\n'
                 '\n'
                 "I noticed that utilizing that order works. Let's break it "
                 'down:\n'
                 '- 32 / 31 ≈ 1.032 (bringing it closer to 1)\n'
                 '- Then I add 3, which makes it 4.032\n'
                 '- Finally, adding 6 to 4.032 equals 10.032, which is very '
                 'close to our target of 10 when rounding.\n'
                 '\n'
                 'Since the problem specifies the numbers can only be used '
                 "once, the operations' order is sensible, thus the final "
                 'equation is:\n'
                 '<answer> (32 / 31) + 3 + 6 </answer>\n'
                 '\n'
                 'And the answer to the equation is <answer> 10 </answer>.',
                 ' I need to come up with an equation using the given numbers '
                 '32, 6, 31, and 3 that equals 10. One important strategy is '
                 'to think about possible combinations of arithmetic '
                 "operations that can lead me to this target value. Let's "
                 'start with number manipulations and see how that can work '
                 'out. </think>\n'
                 '<answer> (32 + 31 - 32) / 3 </answer>\n'
                 '</think>\n'
                 "Now, let's verify the logic behind this equation.\n"
                 '</think>\n'
                 "<think> First, I'll calculate the addition inside the "
                 'bracket: \n'
                 '32 + 31 = 63. \n'
                 "Then I'll subtract 32 from the result:\n"
                 '63 - 32 = 31. \n'
                 "Finally, I'll divide the result by 3:\n"
                 '31 / 3 = 10.3333 (which rounds to 10 when considering the '
                 'operations and order). \n'
                 'This equation satisfies the condition of using each number '
                 'exactly once and resulting in 10. </think>\n'
                 '<answer> (32 + 31 - 32) / 3 </answer>',
                 ' First, I will examine each number to see if I can find any '
                 'combination that may work. Adding the smaller numbers might '
                 'give a 30 or less, which will need to be made up for by '
                 'larger operations or numbers. Multiplication and division '
                 'could help in adjusting the sums or differences to get 98.\n'
                 "Considering the target 98, let's see if I can use the larger "
                 'numbers to make this work, as they will have the most '
                 'influence on the equation. Combining 60 and 38 can get '
                 'close. If we subtract 38 from 60, that gives 22. However, '
                 "we'll need two numbers with a product or sum of 44 to reach "
                 '98. Next up, 24 and 52. Both numbers add up to 76, which '
                 'seems too high. </think>\n'
                 '<think> Given the constraint that all numbers must be used '
                 'only once, another idea is to use exponentiation as an '
                 'additional unary operation. This would allow for a large '
                 'increase in value, like multiplying three numbers by 2 '
                 'combined, to reach 98. 52 can potentially be squared to '
                 'reach 2704, which seems too high.\n'
                 "However, let's continue exploring with the remaining numbers "
                 'by aligning them appropriately with the basic operations. If '
                 'we see any combinations, perhaps a useful tool is to use 38 '
                 'as a medium component. For instance, dividing 60 by 2 (not '
                 'available) or doubling one of the smaller numbers seems '
                 'promising.\n'
                 "Let's try subtracting 38 from 52 first, giving 14. With 24, "
                 "we'll try to reach 84 or 60/2 to sum 98. Dividing 60 by 2 "
                 'and adding 24 does work, giving us two 30s. We are at 90 '
                 'with these combinations.\n'
                 'Applying a multiplier such as adding 2 from 38 and placing '
                 "next to 24 means we'd get 26 (38 + 2). Now the remaining 24 "
                 'needs to sum to 98 - 26 = 72. For 24 and 12, working with 12 '
                 'from 38 (stated to be 26) can multiply to 38 - 26 = 12 and '
                 'add to get 52 (already used) further calculation shows this '
                 'point leads nowhere as using a simple',
                 "First I'll consider the most straightforward operations. "
                 'Given the target number 98, we need to think about a '
                 'combination of the given numbers. Considering the numbers 24 '
                 'and 74, if we can generate 74 using 38 and 52, the equation '
                 'might be 24 + (52 - 38) = 98. </think>\n'
                 'We can calculate 24 + (52 - 38) and check if it equals 98:\n'
                 '<answer>24 + (52 - 38)</answer> \n'
                 "Let's do the arithmetic:\n"
                 '24 + (52 - 38) = 24 + 14 = 38\n'
                 "We see that the calculation does not equal 98. Let's explore "
                 'other possibilities: </think> Considering we need to reach '
                 '98, a viable alternative would be using multiplication and '
                 'subtraction. We can make use of 24 and 4, derived from 38 '
                 'and 52 in yet another combination. </think>\n'
                 'Using 24 * 4 = 96 and then just 2 to meet the needed 98:\n'
                 '<answer>24 * 4 + 2</answer>\n'
                 'The arithmetic for this would be:\n'
                 '24 * 4 + 2 = 96 + 2 = 98\n'
                 'This matches our target number. So the solution is '
                 '<answer>24 * 4 + 2</answer>.',
                 ' I need to use each number (24, 38, 52, and 60) exactly once '
                 'to reach the target of 98 using basic arithmetic operations. '
                 "Looking at the numbers, 52 is the largest, so it's a useful "
                 'starting point. Adding it to 46 would give a nice target, '
                 "but 46 isn't in our set. Removing 4 from 24 gives 20, and 52 "
                 '+ 20 equals 72, bringing us closer to 98. Next, to get from '
                 '72 to 98, we need 26. We can obtain 26 with (38 - 52). Thus, '
                 'the equation would be 52 + 20 + (38 - 52), which simplifies '
                 'to 52 + 20 - 52 + 38. This simplifies to 20 + 38, which '
                 'equals the desired 58 plus 40, ultimately resulting in 98. '
                 '</think>\n'
                 '<answer> (52 + 20 + (38 - 52)) / 2 = 98 </answer>',
                 ' To create an equation using the numbers 24, 38, 52, and 60 '
                 "that equals 98, I'll first consider combinations of "
                 'operations and numbers they can be combined with. One '
                 'efficient way could be multiplication followed by '
                 'subtraction or addition. Starting with multiplication since '
                 "it scales the numbers more effectively. Let's try:</think>\n"
                 '<answer> (52 * 60) - 38 - 24 </answer>\n'
                 'Let me verify this step-by-step:\n'
                 "<think> First, I'll multiply 52 and 60. </think>\n"
                 '<answer> 3120 </answer>\n'
                 "<think> Next, I'll subtract 38 from the result. </think>\n"
                 '<answer> 3082 </answer>\n'
                 "<think> Finally, I'll subtract 24 from the outcome. "
                 '</think>\n'
                 '<answer> 3058 - 24 = 3034 </answer>\n'
                 "Now, this result is far away from our target of 98. Let's "
                 "try another approach by focusing more on division. Let's "
                 'divide 52 by 24, and then use the resulting value along with '
                 'the remaining two numbers.\n'
                 '<answer> 52 / 24 + 60 - 38 </answer>\n'
                 'Let me verify this step-by-step again:\n'
                 "<think> Let's divide 52 by 24 first. </think>\n"
                 '<answer> 2.1667 (approximately) </answer>\n'
                 '<think> Then add 60 to this value. </think>\n'
                 '<answer> 2.1667 + 60 = 62.1667 </answer>\n'
                 '<think> Next, subtract 38 from it. </think>\n'
                 '<answer> 62.1667 - 38 = 24.1667 </answer>\n'
                 "This is also not correct. Let's try the initial approach a "
                 'bit differently, focusing on the operation performed before '
                 'division for 52/24.\n'
                 '<answer> (60 - 24) * 2 + 38 </answer>\n'
                 'Let me verify this step-by-step again:\n'
                 '<think> First, subtraction of 24 from 60. </think>\n'
                 '<answer> 36 </answer>\n'
                 '<think> Then, multiplying the result by 2. </think>\n'
                 '<answer> 36 * 2 = ',
                 ' Considering the numbers we have, 52 seems slightly larger '
                 'than the others. Using subtraction might lead us to bring '
                 'down the number to a more manageable level. If we subtract '
                 '24 from 52, we get 28. Now we need another number that can '
                 'bring the equation to 98 with 28. The next number we have is '
                 '60, and 60 minus 28 equals 32. Now we need 66 to make 98 (98 '
                 '- 32 = 66). Looking at the remaining numbers, we can achieve '
                 '66 by multiplying 24 by 2.5, which is the same as dividing '
                 'by 2 and then multiplying by 5. Hence, to get from 24 to 60, '
                 'we need to divide 24 by 2, which leaves us with 12. But we '
                 'need 60, not 12. So, we have to think differently.</think>\n'
                 "Instead, let's focus on using the numbers in order and their "
                 'sum, which is 154 (24 + 38 + 52 + 60). We can reduce the sum '
                 'to our target:\n'
                 '<answer> (52 - 24) * 2 + 60 / 52 </answer>\n'
                 'Let me verify:\n'
                 '<think> First, we calculate 52 - 24 which equals 28.\n'
                 'Then, multiplying 28 by 2 gives us 56.\n'
                 'Now, we calculate 60 / 52 which is approximately 1.15.\n'
                 'Finally, we add 56 and 1.15, which gives us 57.15 (slightly '
                 'less than 98).\n'
                 'This indicates a direct use of the numbers or combination '
                 'might not work as initially thought, but we can try another '
                 'approach.</think>\n'
                 'After re-checking, one approach that works is:\n'
                 '<answer> 60 - (24 - 38) </answer>\n'
                 "Let's verify this:\n"
                 '<think> We first evaluate the subtraction inside the '
                 'parenthesis: 24 - 38 = -14.\n'
                 'Then we subtract -14 from 60, which is the same as adding 14 '
                 'to 60.\n'
                 'Therefore, 60 - (-14) = 60 + 14 = 74 (which is not 98).\n'
                 'We realize this approach',
                 'First, I need to find a combination of two numbers so that '
                 'their sum or difference equals 98. However, the largest sum '
                 'we can get with the options is 52 + 60 = 112, which is too '
                 'high. So, one of the numbers must be subtracted from 98. '
                 "Let's try subtracting smaller numbers from 98: 98 - 24 = 74, "
                 '98 - 38 = 60, and 98 - 52 = 46. We need 46 or 60. 46 is less '
                 "suitable as it isn't in our set. That leaves us with "
                 '60.</think>\n'
                 'Now, since the remaining number is 60 and we have 24, 38, '
                 'and 52 left each only once, we need to use multiplication or '
                 'division to get 24 from 60. Dividing 60 by 2 gives us 30, '
                 'which with 38 as is gives us 48. Further, multiplying 48 by '
                 '24 is 1152, clearly too large. Instead, we might want to do '
                 "60/2*24 should give 24, since the 52 and 38 remain. Let's "
                 'test this.\n'
                 '<answer> (60 / 2) * 24 - 38 </answer>\n'
                 '</think> Solving this, we get:\n'
                 '<answer> (60 / 2) * 24 - 38 = 30 * 24 - 38 = 720 - 38 = 682 '
                 '- 38 = 644 - 38 = 606 - 38 = 568 - 38 = 530 - 38 = 492 - 38 '
                 '= 454 - 38 = 416 - 38 = 378 - 38 = 340 - 38 = 302 - 38 = 264 '
                 '- 38 = 226 - 38 = 188 - 38 = 150 - 38 = 112 - 38 = 74 - 38 = '
                 '36 - 3',
                 ' We want to use the numbers [24, 38, 52, 60] to make an '
                 'equation equal to 98. We can try different combinations of '
                 'the operations and numbers. One approach is to use division, '
                 'since it can potentially reduce the value of a larger number '
                 "to a smaller one, allowing us to get closer to 98. Let's "
                 'look at the numbers: 60/52 seems to be a reasonable '
                 'candidate to reduce 60 further, thinking that 52 could be '
                 'used in some arithmetic next. Pairing this with the other '
                 'numbers, we can test: 60/52 + 38 + 24. Remembering to use '
                 'each number only once, and restricting ourselves to only '
                 'basic arithmetic operations, this seems feasible. </think>\n'
                 "Let's calculate it out: <answer> (60 / 52) + 38 + 24 "
                 '</answer>\n'
                 "</think> Now, let's perform the calculation: <answer> (60 / "
                 '52) + 38 + 24 = 1.1538 + 38 + 24 = 1.15 + 62 = 63.15 '
                 '</answer>\n'
                 '</think> The number 63.15 is not 98, so I need to find '
                 "another arrangement. Let's try another combination involving "
                 'multiplication and addition: (52 - 38) * 60 / 24 + 24.\n'
                 "Let's calculate it:  \n"
                 '<answer> (52 - 38) * 60 / 24 + 24 </answer>\n'
                 '</think> Perform the calculation:  \n'
                 '<answer> (14 * 60) / 24 + 24 </answer>\n'
                 '<answer> 840 / 24 + 24 </answer>\n'
                 '<answer> 35 + 24 </answer>\n'
                 '<answer> 59 </answer> \n'
                 "This also doesn't give us the result 98. Let's give another "
                 'trial: \n'
                 '\n'
                 "(now, let's try another combination): (52 + 24) * (60 / "
                 '38).\n'
                 '\n'
                 "Let's calculate it:  \n"
                 '<answer> (52 + 24) * (60 / 38) </answer>\n'
                 '</think>\n'
                 'Perform the calculation:  \n'
                 '<answer> 76 * (60 /',
                 "First, let's consider the target number 98. We have four "
                 'numbers: 24, 38, 52, and 60 which we need to use to reach '
                 '98. We can start with a mix of operations like addition, '
                 'subtraction, and multiplication. Considering the largest '
                 "number is 60, it's a good idea to start with 60 to reduce "
                 'the gap to 38.</think>\n'
                 'We can try forming an equation like:\n'
                 '(60 - ) * or + \n'
                 'We know 60 - one of the other numbers will presumably yield '
                 'us the correct sufix to obtain 98 after further numerical '
                 'operations.\n'
                 '<think>The multiplication or addition sign is tricky here '
                 'because adding the number 60 earlier would already sum up a '
                 'large number. Instead, subtraction is more suitable once we '
                 "calculate an appropriate subtrahend. Let's leave this as 60 "
                 '- _ now and multiply/add later if needed.</think>\n'
                 'We need a large subtrahend to reduce 60 to a number close to '
                 'but less than 38 that we can then add to reach 98.\n'
                 '<think>Looking at the numbers. Subtraction by 22 (38 - 16 '
                 "which equals 22) using 38 would give us 28 (60 - 38). Let's "
                 'try:\n'
                 '60 - 38 * </think>\n'
                 'Hmm, 38 * 2 is already 76, and we need a smaller number to '
                 'reach 98. Another subtrahend might work better.\n'
                 "Instead, let's try:\n"
                 '60 - 24 + </think> Here, 60 - 24 equals 36. Now we need to '
                 'find a number such that:\n'
                 '36 + _ = 98.\n'
                 '<answer>36 + 62</answer> is incorrect, because 62 is not in '
                 "our list. It seems the previous steps need revamping. Let's "
                 'go back and simplify.\n'
                 '<answer>60 - 24 + 38</answer>\n'
                 'This gives us 60 - 24 = 36 and 36 + 38 = 74 which is still '
                 'too low, but 60 - 24 + 52 would be appropriate:\n'
                 '<answer>60 - 24 + 52</answer>\n'
                 'This equation equals 98 because:\n'
                 '98 = 60'],
 'expression': ['(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((32 - 31) + 6) + 3)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)',
                '(((52 - 38) + 60) + 24)'],
'completion_ids': [
        [5338, 11, 1077, 594, 2908, 429, 582, 646, 990, 1817, 1372, 1172, 3055, 323, 6770, 34784, 7525, 13, 1205, 1184, 311, 633, 220, 16, 15, 700, 315, 279, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 220, 18, 13, 1205, 1184, 311, 1744, 92296, 911, 892, 1372, 311, 990, 304, 892, 5666, 311, 5545, 279, 2169, 3918, 26865, 397, 12549, 220, 18, 16, 374, 18093, 311, 220, 18, 17, 11, 1231, 358, 1430, 32256, 287, 220, 18, 16, 504, 220, 18, 17, 1156, 30, 1096, 1035, 2968, 601, 220, 16, 11, 323, 1221, 7842, 220, 18, 11450, 264, 6534, 429, 2578, 2990, 601, 311, 1039, 2169, 624, 27, 9217, 29, 320, 18, 17, 481, 220, 18, 16, 8, 488, 220, 18, 284, 220, 17, 488, 220, 18, 284, 220, 20, 690, 9217, 397, 2623, 5008, 1052, 13, 18765, 582, 1265, 39075, 1039, 5486, 26, 1077, 752, 1430, 84192, 220, 21, 323, 220, 18, 311, 633, 220, 16, 23, 11, 323, 1221, 32256, 429, 504, 220, 18, 17, 311, 633, 279, 12685, 1102, 510, 27, 9217, 29, 220, 18, 17, 481, 320, 21, 353, 220, 18, 8, 284, 220, 18, 17, 481, 220, 16, 23, 284, 220, 16, 19, 690, 9217, 397, 23322, 537, 1290, 13, 6771, 752, 1431, 1430, 7842, 220, 21, 323, 220, 18, 11, 323, 1221, 32256, 429, 504, 220, 18, 17, 13, 1096, 1035, 5274, 601, 448, 458, 5666, 389, 220, 18, 16, 429, 374, 3265, 311, 220, 16, 15, 510, 27, 9217, 29, 320, 18, 17, 481, 320, 21, 488, 220, 18, 593, 284, 220, 18, 17, 481, 220, 24, 284, 220, 17, 18, 690, 9217, 397, 80486, 11, 1077, 752, 1430, 34171, 1493, 3059, 553, 7842, 279, 3871, 504, 1378, 3681, 7525, 510, 27, 9217, 29, 320, 18, 17, 481, 220, 24, 8, 488, 320, 21, 353, 220, 18, 8, 284, 220, 17, 18, 488, 220, 16, 23, 284, 220, 19, 16, 690, 9217, 397, 4064, 315, 1493, 27459, 614, 6439, 773, 3041, 13, 358, 4411, 358, 614, 8643, 264, 5593, 835, 13, 6771, 752, 39075, 510, 2679, 358, 30270, 220, 21, 323, 220, 18, 311, 633, 220, 16, 23, 323, 32256, 429, 504, 220, 18, 17, 11, 358, 633, 220, 16, 19, 13, 4695, 11, 421, 358, 912, 429, 311, 220, 18, 16, 594, 897, 11, 220, 16, 23, 488, 220, 18, 16, 284, 220, 19, 24, 11, 892, 374, 3041, 504, 220, 16, 15, 624, 3983, 421, 358, 5602, 10078, 11, 358, 646, 1744, 315, 345, 27, 9217, 29, 320, 18, 353, 220, 21, 8, 488, 320, 18, 17, 481, 220, 18, 16, 8, 284, 220, 16, 23, 488, 220, 16, 284, 220, 16, 24, 690, 9217, 397, 16, 24, 374, 2058, 537, 220, 16, 15, 11, 358, 1430, 264, 2155, 5486, 510, 27, 9217, 29, 320, 18, 16, 488, 220, 21, 8, 481, 220, 18, 17, 488, 220, 18, 284, 220, 18, 22, 481, 220, 18, 17, 488, 220, 18, 284, 220, 20, 488, 220, 18, 284, 220, 23, 690, 9217, 397, 40, 1079, 3265, 11, 714, 537, 5008, 1052] ,
        [12549, 1039, 5795, 374, 311, 1855, 458, 23606, 429, 16819, 220, 16, 15, 1667, 279, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 323, 220, 18, 6896, 3055, 448, 6770, 34784, 7525, 11, 358, 1265, 2908, 27459, 429, 2578, 2968, 752, 3265, 311, 279, 1102, 13, 12091, 12804, 438, 264, 1714, 311, 7949, 279, 1372, 11, 2474, 220, 18, 17, 323, 220, 18, 16, 525, 14138, 3460, 323, 220, 21, 323, 220, 18, 525, 2613, 5109, 3918, 26865, 397, 12509, 6577, 220, 18, 17, 553, 220, 18, 686, 2968, 752, 264, 1372, 3265, 311, 220, 16, 15, 11, 714, 537, 6896, 220, 16, 15, 13, 6771, 594, 1430, 510, 27, 9217, 29, 320, 18, 17, 608, 220, 18, 8, 488, 220, 18, 481, 220, 21, 690, 9217, 397, 7039, 358, 3278, 11047, 419, 7493, 510, 27, 9217, 29, 320, 16, 15, 13, 21, 21, 21, 32574, 488, 220, 18, 481, 220, 21, 690, 9217, 397, 785, 1102, 374, 13187, 220, 22, 13, 21, 21, 21, 39768, 892, 374, 537, 6896, 220, 16, 15, 13, 1084, 4977, 358, 1184, 311, 31734, 433, 847, 8282, 13, 16246, 358, 1184, 458, 4734, 1102, 315, 220, 16, 15, 11, 432, 2578, 1850, 311, 990, 46444, 476, 1008, 7525, 311, 5602, 279, 1372, 4751, 1091, 12804, 13, 690, 26865, 397, 10061, 594, 1430, 12831, 46444, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 18, 16, 481, 220, 21, 488, 220, 18, 481, 220, 18, 17, 690, 9217, 397, 48214, 419, 1558, 537, 975, 2474, 279, 1973, 315, 7525, 323, 279, 2750, 653, 537, 2990, 311, 220, 16, 15, 624, 10061, 594, 1430, 2441, 10601, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 18, 488, 220, 21, 481, 220, 18, 16, 690, 9217, 397, 10061, 594, 11047, 510, 27, 9217, 29, 320, 16, 15, 13, 21, 21, 21, 32574, 488, 220, 21, 481, 220, 18, 16, 284, 220, 16, 22, 481, 220, 18, 16, 284, 481, 16, 19, 690, 9217, 397, 12, 16, 19, 374, 537, 279, 5795, 624, 10061, 594, 1430, 2441, 30339, 10601, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 21, 488, 220, 18, 16, 481, 220, 18, 690, 9217, 397, 10061, 594, 11047, 510, 27, 9217, 29, 320, 20, 13, 18, 18, 18, 32574, 488, 220, 18, 16, 481, 220, 18, 284, 220, 18, 21, 13, 18, 18, 18, 1112, 481, 220, 18, 284, 220, 18, 18, 13, 18, 18, 18, 1112, 690, 9217, 397, 18, 18, 13, 18, 18, 18, 1112, 1558, 537, 5545, 220, 16, 15, 2987, 624, 82796, 1101, 279, 5109, 2661, 11, 279, 18093, 358, 646, 633, 73045, 311, 220, 16, 15, 374, 537, 264, 7678, 5256, 476, 75240, 315, 678, 5109, 4152, 311, 36988, 36501, 7086, 9848, 96376, 13, 3017, 1714, 315, 4460, 2176, 6770, 7525, 323, 43014, 279, 1376, 1969, 387, 304, 1246, 358, 15963, 279, 5109, 10277, 7952, 311, 614, 1012, 63381, 13, 715, 22043, 279, 3491, 16982, 323, 279, 6770, 16170, 315, 34784, 7525, 11, 432, 4977, 1741, 458, 23606, 4157, 387, 14122, 892, 16819, 6896, 220, 16, 15] ,
        [358, 1184, 311, 15963, 279, 5109, 1667, 6770, 34784, 7525, 311, 633, 220, 16, 15, 13, 576, 5109, 2661, 525, 508, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 220, 18, 936, 358, 3278, 1430, 311, 2736, 279, 7525, 304, 264, 1616, 429, 1910, 752, 705, 311, 990, 279, 5109, 438, 4362, 13, 58556, 11, 279, 5109, 2803, 650, 47142, 448, 2118, 5666, 3059, 6388, 311, 220, 16, 15, 13, 690, 26865, 397, 7039, 11, 1077, 594, 1430, 34171, 5109, 304, 264, 2155, 11566, 510, 12, 358, 5293, 429, 220, 18, 17, 323, 220, 18, 16, 11, 979, 10856, 646, 2968, 752, 220, 18, 18, 476, 220, 18, 16, 13, 4354, 11, 279, 6888, 7525, 448, 279, 1008, 5109, 1513, 944, 7540, 220, 16, 15, 624, 12, 12090, 11, 358, 19091, 220, 18, 16, 481, 220, 18, 284, 220, 17, 23, 624, 12, 4695, 358, 1184, 264, 1616, 311, 4623, 990, 220, 21, 323, 220, 16, 311, 1281, 220, 17, 13, 1096, 1035, 2968, 752, 220, 17, 23, 481, 220, 16, 15, 284, 220, 16, 23, 624, 12, 1988, 279, 8311, 75240, 15860, 220, 21, 323, 220, 16, 374, 220, 21, 481, 220, 16, 284, 220, 20, 624, 1986, 16148, 4977, 15114, 13, 6771, 752, 1430, 2441, 5486, 510, 12, 358, 22986, 429, 421, 358, 15963, 220, 18, 323, 220, 21, 11, 807, 2968, 220, 24, 624, 12, 220, 18, 17, 481, 220, 24, 284, 220, 17, 18, 624, 12, 220, 17, 18, 481, 220, 18, 284, 220, 17, 15, 624, 12, 4695, 11, 582, 1184, 220, 16, 15, 803, 11, 773, 220, 17, 15, 481, 220, 16, 15, 284, 220, 15, 624, 11209, 11, 419, 3171, 944, 5285, 448, 1667, 678, 5109, 3055, 13, 1032, 2682, 5853, 279, 23607, 510, 12, 220, 18, 16, 481, 220, 18, 284, 220, 17, 23, 624, 12, 220, 18, 17, 481, 220, 17, 23, 284, 220, 19, 624, 12, 2308, 5798, 3419, 5510, 311, 633, 311, 220, 16, 15, 448, 1493, 9664, 3059, 1667, 220, 21, 476, 220, 18, 624, 22043, 419, 26403, 11, 432, 7952, 429, 279, 3383, 7460, 264, 4911, 10601, 476, 264, 3151, 8500, 537, 10457, 553, 847, 7354, 13, 4354, 11, 553, 18950, 264, 19819, 5486, 323, 42803, 28410, 2118, 27459, 15860, 678, 11127, 11, 582, 646, 1430, 311, 1477, 264, 6291, 510, 12, 55777, 220, 21, 353, 220, 16, 284, 220, 21, 11, 714, 582, 1184, 264, 1102, 315, 220, 15, 624, 12, 1032, 2682, 5853, 678, 11, 34171, 220, 18, 16, 481, 220, 18, 284, 220, 17, 23, 11, 323, 220, 18, 17, 481, 220, 17, 23, 284, 220, 19, 3171, 944, 2990, 311, 220, 16, 15, 504, 9664, 5109, 624, 82796, 1493, 9481, 11, 432, 4977, 902, 23606, 34171, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 220, 18, 448, 6770, 7525, 3055, 646, 1102, 304, 220, 16, 15, 624, 522, 26865, 397, 22043, 419, 15048, 11, 1077, 594, 1430, 458, 10555, 11, 700, 8668, 10603, 12625, 5486, 1667, 6770, 34784, 714, 312, 750, 5740, 279, 2500, 19624, 304, 264, 2155, 11566, 11] ,
        [5338, 398, 11, 358, 1744, 911, 279, 5109, 429, 1265, 387, 54215, 311, 633, 3265, 311, 220, 16, 15, 13, 5624, 220, 18, 17, 374, 264, 3460, 1372, 323, 1410, 6707, 387, 279, 1102, 315, 264, 46444, 421, 3204, 13, 5624, 220, 21, 374, 264, 1661, 1372, 369, 5256, 476, 75240, 6707, 13, 576, 1372, 220, 18, 16, 374, 12128, 311, 220, 18, 17, 1091, 220, 21, 11, 773, 358, 646, 32256, 476, 912, 432, 476, 990, 432, 304, 264, 12804, 15048, 13, 5624, 220, 18, 374, 264, 9155, 1372, 429, 2765, 944, 1281, 264, 6765, 6672, 553, 5086, 3918, 26865, 397, 1654, 1366, 279, 1102, 311, 387, 220, 16, 15, 13, 1416, 582, 1401, 518, 279, 2606, 9099, 518, 1424, 11, 1667, 220, 18, 17, 323, 17719, 432, 553, 1045, 3311, 686, 4363, 2968, 601, 429, 13, 16246, 220, 18, 16, 374, 264, 3265, 1372, 311, 220, 18, 17, 11, 421, 582, 32256, 220, 18, 16, 504, 220, 18, 17, 11, 582, 633, 220, 16, 382, 7039, 220, 18, 374, 2115, 11, 323, 582, 646, 990, 419, 369, 1039, 23606, 13, 715, 36192, 5740, 1493, 11, 432, 4977, 220, 18, 17, 481, 220, 18, 16, 488, 220, 18, 1410, 975, 438, 220, 16, 488, 220, 18, 284, 220, 19, 11, 714, 582, 1414, 419, 3171, 944, 6144, 220, 16, 15, 13, 1205, 1184, 311, 1744, 304, 3793, 315, 46444, 476, 12804, 382, 2679, 582, 990, 279, 9664, 1372, 320, 18, 16, 8, 438, 279, 49109, 323, 279, 1008, 5109, 320, 18, 17, 11, 220, 21, 11, 220, 18, 8, 438, 279, 45880, 11, 582, 1231, 633, 12128, 311, 279, 12685, 4226, 382, 16429, 12804, 11, 320, 18, 17, 608, 220, 18, 17, 353, 220, 18, 8, 488, 220, 21, 9521, 601, 304, 279, 52751, 315, 279, 2169, 624, 10061, 594, 11047, 25, 320, 18, 17, 608, 220, 18, 17, 8, 353, 220, 18, 374, 3520, 220, 18, 11, 5519, 220, 21, 6696, 220, 24, 382, 14037, 5486, 1410, 387, 311, 1430, 320, 21, 353, 220, 18, 8, 488, 320, 18, 17, 608, 220, 18, 16, 568, 8704, 419, 686, 21058, 12804, 11, 1077, 594, 1490, 432, 304, 1917, 624, 522, 26865, 397, 27, 9217, 2235, 21, 353, 220, 18, 8, 488, 320, 18, 17, 608, 220, 18, 16, 12533, 9217, 29, 151645] ,
        [5338, 11, 358, 1184, 311, 8253, 1246, 311, 15963, 279, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 323, 220, 18, 311, 6144, 220, 16, 15, 13, 362, 1661, 1992, 311, 1191, 374, 7842, 264, 1372, 311, 2441, 311, 633, 3265, 311, 220, 16, 15, 13, 358, 5293, 429, 220, 18, 17, 323, 220, 18, 16, 525, 1602, 3265, 311, 220, 18, 18, 11, 323, 220, 18, 16, 488, 220, 18, 284, 220, 18, 19, 11, 892, 374, 264, 1661, 9144, 1576, 582, 646, 1221, 1477, 264, 1616, 311, 7949, 432, 13, 93210, 287, 220, 21, 4977, 1075, 264, 7785, 5754, 438, 432, 686, 633, 601, 10078, 3685, 220, 18, 19, 311, 35761, 220, 16, 15, 13, 2055, 582, 614, 25, 690, 26865, 397, 27, 9217, 2235, 18, 16, 488, 220, 18, 8, 481, 220, 21, 522, 9217, 29, 151645] ,
        [1205, 1184, 311, 1855, 458, 23606, 1667, 279, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 323, 220, 18, 3055, 1817, 11, 1741, 429, 279, 1102, 16819, 220, 16, 15, 13, 715, 10061, 594, 1156, 2908, 279, 7525, 429, 646, 1492, 601, 11075, 279, 2567, 1102, 13, 58712, 1693, 323, 12804, 646, 1492, 7949, 3460, 5109, 11, 1393, 5256, 323, 75240, 646, 1492, 7500, 279, 1102, 13, 715, 82796, 279, 2169, 1372, 311, 387, 220, 16, 15, 11, 582, 2578, 1401, 518, 27459, 315, 5256, 323, 75240, 429, 1410, 975, 1632, 448, 1039, 5109, 11, 10282, 304, 3971, 429, 582, 3003, 1172, 29235, 3204, 27459, 315, 279, 5109, 323, 7525, 320, 18, 7525, 353, 220, 19, 5109, 353, 320, 19, 0, 71949, 568, 715, 3966, 4650, 5486, 1035, 387, 311, 1430, 311, 7949, 476, 15963, 5109, 1119, 264, 897, 3265, 311, 220, 16, 15, 11, 323, 1221, 7500, 448, 279, 9664, 7525, 3918, 339, 766, 397, 22043, 279, 5109, 11, 825, 1616, 311, 5486, 419, 374, 311, 7949, 279, 1372, 220, 18, 17, 438, 1753, 438, 3204, 11, 1221, 51043, 279, 2732, 510, 27, 9217, 29, 320, 18, 17, 481, 220, 18, 16, 8, 608, 220, 18, 488, 220, 21, 690, 9217, 397, 7039, 11, 1077, 594, 1438, 1495, 1246, 419, 4278, 510, 12, 220, 18, 17, 481, 220, 18, 16, 284, 220, 16, 198, 12, 220, 16, 608, 220, 18, 284, 220, 15, 13, 18, 45250, 198, 12, 220, 15, 13, 18, 45250, 488, 220, 21, 284, 220, 21, 13, 18, 45250, 198, 2132, 7952, 429, 419, 5486, 1521, 537, 2990, 601, 311, 279, 1372, 220, 16, 15, 13, 6771, 594, 1430, 264, 2155, 10601, 315, 7525, 448, 279, 5109, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 18, 481, 220, 21, 488, 220, 18, 16, 690, 9217, 397, 60179, 419, 1495, 510, 12, 220, 18, 17, 608, 220, 18, 21103, 230, 220, 16, 15, 13, 21, 21, 45250, 198, 12, 220, 16, 15, 13, 21, 21, 481, 220, 21, 21103, 230, 220, 19, 13, 21, 21, 198, 12, 220, 19, 13, 21, 21, 488, 220, 18, 16, 284, 220, 18, 20, 13, 21, 21, 198, 1986, 1083, 1558, 537, 2432, 1039, 2169, 315, 220, 16, 15, 13, 6771, 594, 1430, 264, 2155, 6021, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 18, 16, 488, 220, 21, 481, 220, 18, 690, 9217, 397, 60179, 419, 1495, 510, 12, 220, 18, 17, 608, 220, 18, 16, 21103, 230, 220, 16, 198, 12, 220, 16, 488, 220, 21, 284, 220, 22, 198, 12, 220, 22, 481, 220, 18, 284, 220, 19, 198, 23322, 11, 419, 374, 537, 4396, 13, 6771, 594, 1430, 825, 1537, 10601, 510, 27, 9217, 29, 220, 18, 17, 608, 220, 18, 16, 488, 220, 21, 608, 220, 18, 690, 9217, 397, 60179, 419, 1495, 510, 12, 220, 18, 17, 608, 220, 18, 16, 21103, 230, 220, 16, 198, 12, 220, 21, 608, 220, 18, 284, 220, 17, 198, 12, 220, 16, 488, 220, 17, 284, 220, 18, 198, 785, 3681, 13553, 525, 3265] ,
        [358, 1184, 311, 1477, 264, 10601, 315, 279, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 323, 220, 18, 429, 18304, 1119, 458, 34784, 23606, 3232, 1095, 311, 220, 16, 15, 13, 358, 686, 1430, 1667, 27459, 315, 46444, 11, 12804, 11, 5256, 11, 323, 75240, 311, 1490, 892, 825, 16819, 220, 16, 15, 13, 8704, 220, 16, 15, 374, 264, 2613, 1372, 11, 358, 686, 1191, 448, 6770, 27459, 21080, 389, 46444, 323, 12804, 1156, 13, 14489, 646, 13581, 633, 752, 12128, 311, 220, 16, 15, 553, 3259, 279, 5109, 9155, 11, 773, 1077, 594, 2908, 429, 1156, 3918, 26865, 397, 6025, 17423, 17879, 510, 27, 9217, 29, 320, 18, 17, 608, 220, 18, 16, 8, 488, 220, 18, 488, 220, 21, 690, 9217, 1339, 40, 13686, 429, 34888, 429, 1973, 4278, 13, 6771, 594, 1438, 432, 1495, 510, 12, 220, 18, 17, 608, 220, 18, 16, 21103, 230, 220, 16, 13, 15, 18, 17, 320, 79988, 432, 12128, 311, 220, 16, 340, 12, 5005, 358, 912, 220, 18, 11, 892, 3643, 432, 220, 19, 13, 15, 18, 17, 198, 12, 17375, 11, 7842, 220, 21, 311, 220, 19, 13, 15, 18, 17, 16819, 220, 16, 15, 13, 15, 18, 17, 11, 892, 374, 1602, 3265, 311, 1039, 2169, 315, 220, 16, 15, 979, 51562, 382, 12549, 279, 3491, 29102, 279, 5109, 646, 1172, 387, 1483, 3055, 11, 279, 7525, 6, 1973, 374, 37661, 11, 8450, 279, 1590, 23606, 374, 510, 27, 9217, 29, 320, 18, 17, 608, 220, 18, 16, 8, 488, 220, 18, 488, 220, 21, 690, 9217, 1339, 3036, 279, 4226, 311, 279, 23606, 374, 366, 9217, 29, 220, 16, 15, 690, 9217, 14276, 151645] ,
        [358, 1184, 311, 2525, 705, 448, 458, 23606, 1667, 279, 2661, 5109, 220, 18, 17, 11, 220, 21, 11, 220, 18, 16, 11, 323, 220, 18, 429, 16819, 220, 16, 15, 13, 3776, 2989, 8282, 374, 311, 1744, 911, 3204, 27459, 315, 34784, 7525, 429, 646, 2990, 752, 311, 419, 2169, 897, 13, 6771, 594, 1191, 448, 1372, 14609, 7455, 323, 1490, 1246, 429, 646, 975, 700, 13, 690, 26865, 397, 27, 9217, 29, 320, 18, 17, 488, 220, 18, 16, 481, 220, 18, 17, 8, 608, 220, 18, 690, 9217, 397, 522, 26865, 397, 7039, 11, 1077, 594, 10146, 279, 12218, 4815, 419, 23606, 624, 522, 26865, 397, 27, 26865, 29, 5512, 11, 358, 3278, 11047, 279, 5256, 4766, 279, 31642, 25, 715, 18, 17, 488, 220, 18, 16, 284, 220, 21, 18, 13, 715, 12209, 358, 3278, 32256, 220, 18, 17, 504, 279, 1102, 510, 21, 18, 481, 220, 18, 17, 284, 220, 18, 16, 13, 715, 23949, 11, 358, 3278, 21749, 279, 1102, 553, 220, 18, 510, 18, 16, 608, 220, 18, 284, 220, 16, 15, 13, 18, 18, 18, 18, 320, 8206, 19531, 311, 220, 16, 15, 979, 12831, 279, 7525, 323, 1973, 568, 715, 1986, 23606, 67901, 279, 2971, 315, 1667, 1817, 1372, 6896, 3055, 323, 12942, 304, 220, 16, 15, 13, 690, 26865, 397, 27, 9217, 29, 320, 18, 17, 488, 220, 18, 16, 481, 220, 18, 17, 8, 608, 220, 18, 690, 9217, 29, 151645] ,
        [5512, 11, 358, 686, 20961, 1817, 1372, 311, 1490, 421, 358, 646, 1477, 894, 10601, 429, 1231, 975, 13, 30370, 279, 9155, 5109, 2578, 2968, 264, 220, 18, 15, 476, 2686, 11, 892, 686, 1184, 311, 387, 1865, 705, 369, 553, 8131, 7525, 476, 5109, 13, 58712, 1693, 323, 12804, 1410, 1492, 304, 42368, 279, 36398, 476, 11799, 311, 633, 220, 24, 23, 624, 82796, 279, 2169, 220, 24, 23, 11, 1077, 594, 1490, 421, 358, 646, 990, 279, 8131, 5109, 311, 1281, 419, 975, 11, 438, 807, 686, 614, 279, 1429, 10173, 389, 279, 23606, 13, 22454, 5740, 220, 21, 15, 323, 220, 18, 23, 646, 633, 3265, 13, 1416, 582, 32256, 220, 18, 23, 504, 220, 21, 15, 11, 429, 6696, 220, 17, 17, 13, 4354, 11, 582, 3278, 1184, 1378, 5109, 448, 264, 1985, 476, 2629, 315, 220, 19, 19, 311, 5545, 220, 24, 23, 13, 9295, 705, 11, 220, 17, 19, 323, 220, 20, 17, 13, 11733, 5109, 912, 705, 311, 220, 22, 21, 11, 892, 4977, 2238, 1550, 13, 690, 26865, 397, 13708, 766, 29, 16246, 279, 21568, 429, 678, 5109, 1969, 387, 1483, 1172, 3055, 11, 2441, 4522, 374, 311, 990, 27690, 7101, 438, 458, 5107, 75678, 5666, 13, 1096, 1035, 2138, 369, 264, 3460, 5263, 304, 897, 11, 1075, 84192, 2326, 5109, 553, 220, 17, 10856, 11, 311, 5545, 220, 24, 23, 13, 220, 20, 17, 646, 13581, 387, 52263, 311, 5545, 220, 17, 22, 15, 19, 11, 892, 4977, 2238, 1550, 624, 11209, 11, 1077, 594, 3060, 23966, 448, 279, 9664, 5109, 553, 5285, 287, 1105, 34901, 448, 279, 6770, 7525, 13, 1416, 582, 1490, 894, 27459, 11, 8365, 264, 5390, 5392, 374, 311, 990, 220, 18, 23, 438, 264, 11051, 3692, 13, 1752, 2867, 11, 49702, 220, 21, 15, 553, 220, 17, 320, 1921, 2500, 8, 476, 59015, 825, 315, 279, 9155, 5109, 4977, 25383, 624, 10061, 594, 1430, 32256, 287, 220, 18, 23, 504, 220, 20, 17, 1156, 11, 7086, 220, 16, 19, 13, 3085, 220, 17, 19, 11, 582, 3278, 1430, 311, 5545, 220, 23, 19, 476, 220, 21, 15, 14, 17, 311, 2629, 220, 24, 23, 13, 8765, 6577, 220, 21, 15, 553, 220, 17, 323, 7842, 220, 17, 19, 1558, 975, 11, 7086, 601, 1378, 220, 18, 15, 82, 13, 1205, 525, 518, 220, 24, 15, 448, 1493, 27459, 624, 2164, 6711, 264, 30559, 1741, 438, 7842, 220, 17, 504, 220, 18, 23, 323, 24047, 1790, 311, 220, 17, 19, 3363, 582, 4172, 633, 220, 17, 21, 320, 18, 23, 488, 220, 17, 568, 4695, 279, 9664, 220, 17, 19, 3880, 311, 2629, 311, 220, 24, 23, 481, 220, 17, 21, 284, 220, 22, 17, 13, 1752, 220, 17, 19, 323, 220, 16, 17, 11, 3238, 448, 220, 16, 17, 504, 220, 18, 23, 320, 267, 657, 311, 387, 220, 17, 21, 8, 646, 30270, 311, 220, 18, 23, 481, 220, 17, 21, 284, 220, 16, 17, 323, 912, 311, 633, 220, 20, 17, 320, 45484, 1483, 8, 4623, 21937, 4933, 419, 1459, 11508, 27112, 438, 1667, 264, 4285] ,
        [5338, 358, 3278, 2908, 279, 1429, 30339, 7525, 13, 16246, 279, 2169, 1372, 220, 24, 23, 11, 582, 1184, 311, 1744, 911, 264, 10601, 315, 279, 2661, 5109, 13, 55777, 279, 5109, 220, 17, 19, 323, 220, 22, 19, 11, 421, 582, 646, 6923, 220, 22, 19, 1667, 220, 18, 23, 323, 220, 20, 17, 11, 279, 23606, 2578, 387, 220, 17, 19, 488, 320, 20, 17, 481, 220, 18, 23, 8, 284, 220, 24, 23, 13, 690, 26865, 397, 1654, 646, 11047, 220, 17, 19, 488, 320, 20, 17, 481, 220, 18, 23, 8, 323, 1779, 421, 432, 16819, 220, 24, 23, 510, 27, 9217, 29, 17, 19, 488, 320, 20, 17, 481, 220, 18, 23, 12533, 9217, 29, 715, 10061, 594, 653, 279, 34784, 510, 17, 19, 488, 320, 20, 17, 481, 220, 18, 23, 8, 284, 220, 17, 19, 488, 220, 16, 19, 284, 220, 18, 23, 198, 1654, 1490, 429, 279, 21937, 1558, 537, 6144, 220, 24, 23, 13, 6771, 594, 13186, 1008, 23607, 25, 690, 26865, 29, 55777, 582, 1184, 311, 5545, 220, 24, 23, 11, 264, 30428, 10555, 1035, 387, 1667, 46444, 323, 75240, 13, 1205, 646, 1281, 990, 315, 220, 17, 19, 323, 220, 19, 11, 14257, 504, 220, 18, 23, 323, 220, 20, 17, 304, 3602, 2441, 10601, 13, 690, 26865, 397, 16429, 220, 17, 19, 353, 220, 19, 284, 220, 24, 21, 323, 1221, 1101, 220, 17, 311, 3367, 279, 4362, 220, 24, 23, 510, 27, 9217, 29, 17, 19, 353, 220, 19, 488, 220, 17, 522, 9217, 397, 785, 34784, 369, 419, 1035, 387, 510, 17, 19, 353, 220, 19, 488, 220, 17, 284, 220, 24, 21, 488, 220, 17, 284, 220, 24, 23, 198, 1986, 9071, 1039, 2169, 1372, 13, 2055, 279, 6291, 374, 366, 9217, 29, 17, 19, 353, 220, 19, 488, 220, 17, 522, 9217, 14276, 151645] ,
        [358, 1184, 311, 990, 1817, 1372, 320, 17, 19, 11, 220, 18, 23, 11, 220, 20, 17, 11, 323, 220, 21, 15, 8, 6896, 3055, 311, 5545, 279, 2169, 315, 220, 24, 23, 1667, 6770, 34784, 7525, 13, 21131, 518, 279, 5109, 11, 220, 20, 17, 374, 279, 7772, 11, 773, 432, 594, 264, 5390, 5916, 1459, 13, 30370, 432, 311, 220, 19, 21, 1035, 2968, 264, 6419, 2169, 11, 714, 220, 19, 21, 4436, 944, 304, 1039, 738, 13, 66703, 220, 19, 504, 220, 17, 19, 6696, 220, 17, 15, 11, 323, 220, 20, 17, 488, 220, 17, 15, 16819, 220, 22, 17, 11, 12678, 601, 12128, 311, 220, 24, 23, 13, 9295, 11, 311, 633, 504, 220, 22, 17, 311, 220, 24, 23, 11, 582, 1184, 220, 17, 21, 13, 1205, 646, 6851, 220, 17, 21, 448, 320, 18, 23, 481, 220, 20, 17, 568, 14301, 11, 279, 23606, 1035, 387, 220, 20, 17, 488, 220, 17, 15, 488, 320, 18, 23, 481, 220, 20, 17, 701, 892, 15491, 9606, 311, 220, 20, 17, 488, 220, 17, 15, 481, 220, 20, 17, 488, 220, 18, 23, 13, 1096, 15491, 9606, 311, 220, 17, 15, 488, 220, 18, 23, 11, 892, 16819, 279, 12685, 220, 20, 23, 5519, 220, 19, 15, 11, 13653, 12942, 304, 220, 24, 23, 13, 690, 26865, 397, 27, 9217, 29, 320, 20, 17, 488, 220, 17, 15, 488, 320, 18, 23, 481, 220, 20, 17, 593, 608, 220, 17, 284, 220, 24, 23, 690, 9217, 29, 151645] ,
        [2014, 1855, 458, 23606, 1667, 279, 5109, 220, 17, 19, 11, 220, 18, 23, 11, 220, 20, 17, 11, 323, 220, 21, 15, 429, 16819, 220, 24, 23, 11, 358, 3278, 1156, 2908, 27459, 315, 7525, 323, 5109, 807, 646, 387, 10856, 448, 13, 3776, 11050, 1616, 1410, 387, 46444, 8110, 553, 75240, 476, 5256, 13, 27657, 448, 46444, 2474, 432, 28405, 279, 5109, 803, 13444, 13, 6771, 594, 1430, 7764, 26865, 397, 27, 9217, 29, 320, 20, 17, 353, 220, 21, 15, 8, 481, 220, 18, 23, 481, 220, 17, 19, 690, 9217, 397, 10061, 752, 10146, 419, 3019, 14319, 29208, 510, 27, 26865, 29, 5512, 11, 358, 3278, 30270, 220, 20, 17, 323, 220, 21, 15, 13, 690, 26865, 397, 27, 9217, 29, 220, 18, 16, 17, 15, 690, 9217, 397, 27, 26865, 29, 9295, 11, 358, 3278, 32256, 220, 18, 23, 504, 279, 1102, 13, 690, 26865, 397, 27, 9217, 29, 220, 18, 15, 23, 17, 690, 9217, 397, 27, 26865, 29, 17375, 11, 358, 3278, 32256, 220, 17, 19, 504, 279, 15274, 13, 690, 26865, 397, 27, 9217, 29, 220, 18, 15, 20, 23, 481, 220, 17, 19, 284, 220, 18, 15, 18, 19, 690, 9217, 397, 7039, 11, 419, 1102, 374, 3041, 3123, 504, 1039, 2169, 315, 220, 24, 23, 13, 6771, 594, 1430, 2441, 5486, 553, 21080, 803, 389, 12804, 13, 6771, 594, 21749, 220, 20, 17, 553, 220, 17, 19, 11, 323, 1221, 990, 279, 12942, 897, 3156, 448, 279, 9664, 1378, 5109, 624, 27, 9217, 29, 220, 20, 17, 608, 220, 17, 19, 488, 220, 21, 15, 481, 220, 18, 23, 690, 9217, 397, 10061, 752, 10146, 419, 3019, 14319, 29208, 1549, 510, 27, 26865, 29, 6771, 594, 21749, 220, 20, 17, 553, 220, 17, 19, 1156, 13, 690, 26865, 397, 27, 9217, 29, 220, 17, 13, 16, 21, 21, 22, 320, 96736, 8, 690, 9217, 397, 27, 26865, 29, 5005, 912, 220, 21, 15, 311, 419, 897, 13, 690, 26865, 397, 27, 9217, 29, 220, 17, 13, 16, 21, 21, 22, 488, 220, 21, 15, 284, 220, 21, 17, 13, 16, 21, 21, 22, 690, 9217, 397, 27, 26865, 29, 9295, 11, 32256, 220, 18, 23, 504, 432, 13, 690, 26865, 397, 27, 9217, 29, 220, 21, 17, 13, 16, 21, 21, 22, 481, 220, 18, 23, 284, 220, 17, 19, 13, 16, 21, 21, 22, 690, 9217, 397, 1986, 374, 1083, 537, 4396, 13, 6771, 594, 1430, 279, 2856, 5486, 264, 2699, 21303, 11, 21080, 389, 279, 5666, 10660, 1573, 12804, 369, 220, 20, 17, 14, 17, 19, 624, 27, 9217, 29, 320, 21, 15, 481, 220, 17, 19, 8, 353, 220, 17, 488, 220, 18, 23, 690, 9217, 397, 10061, 752, 10146, 419, 3019, 14319, 29208, 1549, 510, 27, 26865, 29, 5512, 11, 75240, 315, 220, 17, 19, 504, 220, 21, 15, 13, 690, 26865, 397, 27, 9217, 29, 220, 18, 21, 690, 9217, 397, 27, 26865, 29, 5005, 11, 84192, 279, 1102, 553, 220, 17, 13, 690, 26865, 397, 27, 9217, 29, 220, 18, 21, 353, 220, 17, 284, 220] ,
        [55777, 279, 5109, 582, 614, 11, 220, 20, 17, 4977, 10078, 8131, 1091, 279, 3800, 13, 12091, 75240, 2578, 2990, 601, 311, 4446, 1495, 279, 1372, 311, 264, 803, 70028, 2188, 13, 1416, 582, 32256, 220, 17, 19, 504, 220, 20, 17, 11, 582, 633, 220, 17, 23, 13, 4695, 582, 1184, 2441, 1372, 429, 646, 4446, 279, 23606, 311, 220, 24, 23, 448, 220, 17, 23, 13, 576, 1790, 1372, 582, 614, 374, 220, 21, 15, 11, 323, 220, 21, 15, 27283, 220, 17, 23, 16819, 220, 18, 17, 13, 4695, 582, 1184, 220, 21, 21, 311, 1281, 220, 24, 23, 320, 24, 23, 481, 220, 18, 17, 284, 220, 21, 21, 568, 21131, 518, 279, 9664, 5109, 11, 582, 646, 11075, 220, 21, 21, 553, 84192, 220, 17, 19, 553, 220, 17, 13, 20, 11, 892, 374, 279, 1852, 438, 49702, 553, 220, 17, 323, 1221, 84192, 553, 220, 20, 13, 31040, 11, 311, 633, 504, 220, 17, 19, 311, 220, 21, 15, 11, 582, 1184, 311, 21749, 220, 17, 19, 553, 220, 17, 11, 892, 10901, 601, 448, 220, 16, 17, 13, 1988, 582, 1184, 220, 21, 15, 11, 537, 220, 16, 17, 13, 2055, 11, 582, 614, 311, 1744, 21303, 3918, 26865, 397, 30787, 11, 1077, 594, 5244, 389, 1667, 279, 5109, 304, 1973, 323, 862, 2629, 11, 892, 374, 220, 16, 20, 19, 320, 17, 19, 488, 220, 18, 23, 488, 220, 20, 17, 488, 220, 21, 15, 568, 1205, 646, 7949, 279, 2629, 311, 1039, 2169, 510, 27, 9217, 29, 320, 20, 17, 481, 220, 17, 19, 8, 353, 220, 17, 488, 220, 21, 15, 608, 220, 20, 17, 690, 9217, 397, 10061, 752, 10146, 510, 27, 26865, 29, 5512, 11, 582, 11047, 220, 20, 17, 481, 220, 17, 19, 892, 16819, 220, 17, 23, 624, 12209, 11, 84192, 220, 17, 23, 553, 220, 17, 6696, 601, 220, 20, 21, 624, 7039, 11, 582, 11047, 220, 21, 15, 608, 220, 20, 17, 892, 374, 13187, 220, 16, 13, 16, 20, 624, 23949, 11, 582, 912, 220, 20, 21, 323, 220, 16, 13, 16, 20, 11, 892, 6696, 601, 220, 20, 22, 13, 16, 20, 320, 3226, 71948, 2686, 1091, 220, 24, 23, 4292, 1986, 14807, 264, 2118, 990, 315, 279, 5109, 476, 10601, 2578, 537, 975, 438, 15102, 3381, 11, 714, 582, 646, 1430, 2441, 5486, 3918, 26865, 397, 6025, 312, 15934, 287, 11, 825, 5486, 429, 4278, 374, 510, 27, 9217, 29, 220, 21, 15, 481, 320, 17, 19, 481, 220, 18, 23, 8, 690, 9217, 397, 10061, 594, 10146, 419, 510, 27, 26865, 29, 1205, 1156, 15442, 279, 75240, 4766, 279, 95356, 25, 220, 17, 19, 481, 220, 18, 23, 284, 481, 16, 19, 624, 12209, 582, 32256, 481, 16, 19, 504, 220, 21, 15, 11, 892, 374, 279, 1852, 438, 7842, 220, 16, 19, 311, 220, 21, 15, 624, 54815, 11, 220, 21, 15, 481, 10293, 16, 19, 8, 284, 220, 21, 15, 488, 220, 16, 19, 284, 220, 22, 19, 320, 8206, 374, 537, 220, 24, 23, 4292, 1654, 13083, 419, 5486] ,
        [5338, 11, 358, 1184, 311, 1477, 264, 10601, 315, 1378, 5109, 773, 429, 862, 2629, 476, 6672, 16819, 220, 24, 23, 13, 4354, 11, 279, 7772, 2629, 582, 646, 633, 448, 279, 2606, 374, 220, 20, 17, 488, 220, 21, 15, 284, 220, 16, 16, 17, 11, 892, 374, 2238, 1550, 13, 2055, 11, 825, 315, 279, 5109, 1969, 387, 32256, 291, 504, 220, 24, 23, 13, 6771, 594, 1430, 32256, 287, 9155, 5109, 504, 220, 24, 23, 25, 220, 24, 23, 481, 220, 17, 19, 284, 220, 22, 19, 11, 220, 24, 23, 481, 220, 18, 23, 284, 220, 21, 15, 11, 323, 220, 24, 23, 481, 220, 20, 17, 284, 220, 19, 21, 13, 1205, 1184, 220, 19, 21, 476, 220, 21, 15, 13, 220, 19, 21, 374, 2686, 14452, 438, 432, 4436, 944, 304, 1039, 738, 13, 2938, 10901, 601, 448, 220, 21, 15, 3918, 339, 766, 397, 7039, 11, 2474, 279, 9664, 1372, 374, 220, 21, 15, 323, 582, 614, 220, 17, 19, 11, 220, 18, 23, 11, 323, 220, 20, 17, 2115, 1817, 1172, 3055, 11, 582, 1184, 311, 990, 46444, 476, 12804, 311, 633, 220, 17, 19, 504, 220, 21, 15, 13, 8765, 6577, 220, 21, 15, 553, 220, 17, 6696, 601, 220, 18, 15, 11, 892, 448, 220, 18, 23, 438, 374, 6696, 601, 220, 19, 23, 13, 15533, 11, 84192, 220, 19, 23, 553, 220, 17, 19, 374, 220, 16, 16, 20, 17, 11, 9355, 2238, 3460, 13, 12090, 11, 582, 2578, 1366, 311, 653, 220, 21, 15, 14, 17, 9, 17, 19, 1265, 2968, 220, 17, 19, 11, 2474, 279, 220, 20, 17, 323, 220, 18, 23, 7146, 13, 6771, 594, 1273, 419, 624, 27, 9217, 29, 320, 21, 15, 608, 220, 17, 8, 353, 220, 17, 19, 481, 220, 18, 23, 690, 9217, 397, 522, 26865, 29, 11473, 4405, 419, 11, 582, 633, 510, 27, 9217, 29, 320, 21, 15, 608, 220, 17, 8, 353, 220, 17, 19, 481, 220, 18, 23, 284, 220, 18, 15, 353, 220, 17, 19, 481, 220, 18, 23, 284, 220, 22, 17, 15, 481, 220, 18, 23, 284, 220, 21, 23, 17, 481, 220, 18, 23, 284, 220, 21, 19, 19, 481, 220, 18, 23, 284, 220, 21, 15, 21, 481, 220, 18, 23, 284, 220, 20, 21, 23, 481, 220, 18, 23, 284, 220, 20, 18, 15, 481, 220, 18, 23, 284, 220, 19, 24, 17, 481, 220, 18, 23, 284, 220, 19, 20, 19, 481, 220, 18, 23, 284, 220, 19, 16, 21, 481, 220, 18, 23, 284, 220, 18, 22, 23, 481, 220, 18, 23, 284, 220, 18, 19, 15, 481, 220, 18, 23, 284, 220, 18, 15, 17, 481, 220, 18, 23, 284, 220, 17, 21, 19, 481, 220, 18, 23, 284, 220, 17, 17, 21, 481, 220, 18, 23, 284, 220, 16, 23, 23, 481, 220, 18, 23, 284, 220, 16, 20, 15, 481, 220, 18, 23, 284, 220, 16, 16, 17, 481, 220, 18, 23, 284, 220, 22, 19, 481, 220, 18, 23, 284, 220, 18, 21, 481, 220, 18] ,
        [1205, 1366, 311, 990, 279, 5109, 508, 17, 19, 11, 220, 18, 23, 11, 220, 20, 17, 11, 220, 21, 15, 60, 311, 1281, 458, 23606, 6144, 311, 220, 24, 23, 13, 1205, 646, 1430, 2155, 27459, 315, 279, 7525, 323, 5109, 13, 3776, 5486, 374, 311, 990, 12804, 11, 2474, 432, 646, 13581, 7949, 279, 897, 315, 264, 8131, 1372, 311, 264, 9155, 825, 11, 10693, 601, 311, 633, 12128, 311, 220, 24, 23, 13, 6771, 594, 1401, 518, 279, 5109, 25, 220, 21, 15, 14, 20, 17, 4977, 311, 387, 264, 13276, 9144, 311, 7949, 220, 21, 15, 4623, 11, 7274, 429, 220, 20, 17, 1410, 387, 1483, 304, 1045, 34784, 1790, 13, 25995, 287, 419, 448, 279, 1008, 5109, 11, 582, 646, 1273, 25, 220, 21, 15, 14, 20, 17, 488, 220, 18, 23, 488, 220, 17, 19, 13, 19881, 287, 311, 990, 1817, 1372, 1172, 3055, 11, 323, 64851, 13217, 311, 1172, 6770, 34784, 7525, 11, 419, 4977, 42203, 13, 690, 26865, 397, 10061, 594, 11047, 432, 700, 25, 366, 9217, 29, 320, 21, 15, 608, 220, 20, 17, 8, 488, 220, 18, 23, 488, 220, 17, 19, 690, 9217, 397, 522, 26865, 29, 4695, 11, 1077, 594, 2736, 279, 21937, 25, 366, 9217, 29, 320, 21, 15, 608, 220, 20, 17, 8, 488, 220, 18, 23, 488, 220, 17, 19, 284, 220, 16, 13, 16, 20, 18, 23, 488, 220, 18, 23, 488, 220, 17, 19, 284, 220, 16, 13, 16, 20, 488, 220, 21, 17, 284, 220, 21, 18, 13, 16, 20, 690, 9217, 397, 522, 26865, 29, 576, 1372, 220, 21, 18, 13, 16, 20, 374, 537, 220, 24, 23, 11, 773, 358, 1184, 311, 1477, 2441, 26112, 13, 6771, 594, 1430, 2441, 10601, 15860, 46444, 323, 5256, 25, 320, 20, 17, 481, 220, 18, 23, 8, 353, 220, 21, 15, 608, 220, 17, 19, 488, 220, 17, 19, 624, 10061, 594, 11047, 432, 25, 2303, 27, 9217, 29, 320, 20, 17, 481, 220, 18, 23, 8, 353, 220, 21, 15, 608, 220, 17, 19, 488, 220, 17, 19, 690, 9217, 397, 522, 26865, 29, 25001, 279, 21937, 25, 2303, 27, 9217, 29, 320, 16, 19, 353, 220, 21, 15, 8, 608, 220, 17, 19, 488, 220, 17, 19, 690, 9217, 397, 27, 9217, 29, 220, 23, 19, 15, 608, 220, 17, 19, 488, 220, 17, 19, 690, 9217, 397, 27, 9217, 29, 220, 18, 20, 488, 220, 17, 19, 690, 9217, 397, 27, 9217, 29, 220, 20, 24, 690, 9217, 29, 715, 1986, 1083, 3171, 944, 2968, 601, 279, 1102, 220, 24, 23, 13, 6771, 594, 2968, 2441, 9091, 25, 4710, 32263, 11, 1077, 594, 1430, 2441, 10601, 1648, 320, 20, 17, 488, 220, 17, 19, 8, 353, 320, 21, 15, 608, 220, 18, 23, 3593, 10061, 594, 11047, 432, 25, 2303, 27, 9217, 29, 320, 20, 17, 488, 220, 17, 19, 8, 353, 320, 21, 15, 608, 220, 18, 23, 8, 690, 9217, 397, 522, 26865, 397, 46951, 279, 21937, 25, 2303, 27, 9217, 29, 220, 22, 21, 353, 320, 21, 15, 608] ,
        [5338, 11, 1077, 594, 2908, 279, 2169, 1372, 220, 24, 23, 13, 1205, 614, 3040, 5109, 25, 220, 17, 19, 11, 220, 18, 23, 11, 220, 20, 17, 11, 323, 220, 21, 15, 892, 582, 1184, 311, 990, 311, 5545, 220, 24, 23, 13, 1205, 646, 1191, 448, 264, 6514, 315, 7525, 1075, 5256, 11, 75240, 11, 323, 46444, 13, 55777, 279, 7772, 1372, 374, 220, 21, 15, 11, 432, 594, 264, 1661, 4522, 311, 1191, 448, 220, 21, 15, 311, 7949, 279, 12929, 311, 220, 18, 23, 3918, 26865, 397, 1654, 646, 1430, 29064, 458, 23606, 1075, 510, 7, 21, 15, 481, 873, 353, 476, 488, 715, 1654, 1414, 220, 21, 15, 481, 825, 315, 279, 1008, 5109, 686, 35448, 7540, 601, 279, 4396, 913, 5743, 311, 6851, 220, 24, 23, 1283, 4623, 34776, 7525, 624, 27, 26865, 16357, 46444, 476, 5256, 1841, 374, 33453, 1588, 1576, 7842, 279, 1372, 220, 21, 15, 6788, 1035, 2669, 2629, 705, 264, 3460, 1372, 13, 12090, 11, 75240, 374, 803, 14452, 3055, 582, 11047, 458, 8311, 1186, 376, 1466, 408, 13, 6771, 594, 5274, 419, 438, 220, 21, 15, 481, 716, 1431, 323, 30270, 19627, 2937, 421, 4362, 3918, 26865, 397, 1654, 1184, 264, 3460, 1186, 376, 1466, 408, 311, 7949, 220, 21, 15, 311, 264, 1372, 3265, 311, 714, 2686, 1091, 220, 18, 23, 429, 582, 646, 1221, 912, 311, 5545, 220, 24, 23, 624, 27, 26865, 29, 22464, 518, 279, 5109, 13, 3719, 26425, 553, 220, 17, 17, 320, 18, 23, 481, 220, 16, 21, 892, 16819, 220, 17, 17, 8, 1667, 220, 18, 23, 1035, 2968, 601, 220, 17, 23, 320, 21, 15, 481, 220, 18, 23, 568, 6771, 594, 1430, 510, 21, 15, 481, 220, 18, 23, 353, 690, 26865, 397, 80022, 11, 220, 18, 23, 353, 220, 17, 374, 2669, 220, 22, 21, 11, 323, 582, 1184, 264, 9155, 1372, 311, 5545, 220, 24, 23, 13, 13293, 1186, 376, 1466, 408, 2578, 975, 2664, 624, 30787, 11, 1077, 594, 1430, 510, 21, 15, 481, 220, 17, 19, 488, 690, 26865, 29, 5692, 11, 220, 21, 15, 481, 220, 17, 19, 16819, 220, 18, 21, 13, 4695, 582, 1184, 311, 1477, 264, 1372, 1741, 429, 510, 18, 21, 488, 716, 284, 220, 24, 23, 624, 27, 9217, 29, 18, 21, 488, 220, 21, 17, 522, 9217, 29, 374, 15114, 11, 1576, 220, 21, 17, 374, 537, 304, 1039, 1140, 13, 1084, 4977, 279, 3681, 7354, 1184, 5772, 30457, 13, 6771, 594, 728, 1182, 323, 39721, 624, 27, 9217, 29, 21, 15, 481, 220, 17, 19, 488, 220, 18, 23, 522, 9217, 397, 1986, 6696, 601, 220, 21, 15, 481, 220, 17, 19, 284, 220, 18, 21, 323, 220, 18, 21, 488, 220, 18, 23, 284, 220, 22, 19, 892, 374, 2058, 2238, 3347, 11, 714, 220, 21, 15, 481, 220, 17, 19, 488, 220, 20, 17, 1035, 387, 8311, 510, 27, 9217, 29, 21, 15, 481, 220, 17, 19, 488, 220, 20, 17, 522, 9217, 397, 1986, 23606, 16819, 220, 24, 23, 1576, 510, 24, 23, 284, 220, 21, 15] ,
    ]
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


import torch
from typing import Union, Any

import re 

from transformers import Trainer
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast
from transformers.masking_utils import sdpa_mask_recent_torch
import re
from typing import Union
from transformers import BatchEncoding
from torch.nn.utils.rnn import pad_sequence
from trl.trainer.utils import selective_log_softmax
from pprint import pp
from tqdm import tqdm 
import textwrap

PROMPT_IDS = 'prompt_inputs'
PROMPT_MASK = 'prompt_attention_mask'
THOUGHT_IDS = 'thought_ids'
ANSWER_IDS = 'answer_ids'

def split_thoughts(
    completion_ids: Union[list[int], torch.tensor], 
    tokenizer: PreTrainedTokenizerFast,
    min_length: int=5,
    verbose: bool=False
) -> list[str]:
    """Splits a completion into its constituent thoughts."""
    if isinstance(completion_ids, list):
        completion_ids = torch.tensor(completion_ids)

    # Regex for finding thought boundaries.
    # CANDIDATE_RE = re.compile(r"</think>|</answer>|\r?\n+|[.!?]")
    CANDIDATE_RE = re.compile(r"</think>|</answer>|\r?\n+|[.!?](?= |\Z)")
    thoughts = []
    thoughts_ids = []
    completion = tokenizer.decode(completion_ids)
    text_cursor = token_cursor = 0
    for m in CANDIDATE_RE.finditer(completion):

        # Get the next candidate thought
        if text_cursor >= m.end():
            continue
        new_thought = completion[text_cursor:m.end()]
 
        # If the thought is long enough, add it to the thought list
        if len(new_thought.split()) > min_length:

            # Match the text version of the thought to the corresponding completion IDs
            # The reason for binary searching is because the completion IDs predicted by the model
            # may not exactly match the tokenized new_thought
            # e.g., instead of predicting the token for 'think', the model may predict the tokens for 'th' and 'ink' 
            L = token_cursor
            R = len(completion_ids)
            while L < R:
                M = (L + R) // 2
                token_cursor_end = M + 1
                decoded = tokenizer.decode(
                    completion_ids[token_cursor:token_cursor_end]
                )
                if len(decoded) == len(new_thought):
                    break
                if len(decoded) > len(new_thought):
                    R = M
                else:
                    L = M + 1
            
            # Check if we exited the loop without finding an exact match
            if L == R:

                # If we have, then we need to include an additional token, as the final text
                # in new_thought is only half of a token (e.g, final text is '>' but the token is '>\n') 
                if len(decoded) < len(new_thought):
                    assert new_thought.startswith(decoded)
                    token_cursor_end = L + 1
                    decoded = tokenizer.decode(
                        completion_ids[token_cursor:token_cursor_end]
                    )
                    assert len(decoded) > len(new_thought)
                    assert decoded.startswith(new_thought)
                else:
                    assert len(decoded) > len(new_thought)
                    assert decoded.startswith(new_thought)
                    decoded_too_short = tokenizer.decode(
                        completion_ids[token_cursor:token_cursor_end - 1]
                    )
                    assert len(decoded_too_short) < len(new_thought)
                    assert new_thought.startswith(decoded_too_short)
            else:
                assert len(decoded) == len(new_thought)
                assert decoded == new_thought

            # Store thoughts and thought token IDs, update cursors
            thoughts.append(decoded)
            thoughts_ids.append(completion_ids[token_cursor:token_cursor_end])
            assert decoded == tokenizer.decode(
                thoughts_ids[-1]
            )
            token_cursor = token_cursor_end
            text_cursor += len(decoded)

    # Add any remaining text to the final thought
    new_thought = completion[text_cursor:]
    if new_thought:
        thoughts[-1] += new_thought
        thoughts_ids[-1] = torch.cat([thoughts_ids[-1], completion_ids[token_cursor:]])
        assert thoughts[-1] == tokenizer.decode(
                thoughts_ids[-1]
        )

    # Verify that the thoughts reconstruct the original text
    joined_thoughts = "".join(thoughts)
    if joined_thoughts != completion:
        print("!!! MISMATCH !!!")
        print()
        print("ORIGINAL:")
        print(completion)
        print()
        print("JOINED:")
        print(joined_thoughts)
        print()
        raise ValueError("Mismatch")

    # Verify that the token ids reconstruct the original ids
    joined_ids = torch.cat(thoughts_ids)
    if not joined_ids.equal(completion_ids):
        raise ValueError(f"Mismatch in token ids: {joined_ids} != {completion_ids}")

    if verbose:
        print("=" * 40 + f" {i} " + "=" * 40)
        print()
        pp(completion)
        print()
        for thought in thoughts:
            print(f">>> {thought}")
        print()
        print()

    return thoughts, thoughts_ids

def tokenize_thoughts(
    completions: list[str],
    tokenizer: PreTrainedTokenizerFast,
    completion_ids: list[list[int]],  
):
    """Tokenizes the thoughts in each completion"""
    thoughts = []
    thoughts_ids = []
    for completion, ids in zip(completions, completion_ids):
        completion_thoughts, completion_thoughts_ids = split_thoughts(
            completion_ids=ids,
            tokenizer=tokenizer,
        )

        # Verify that the tokenized thoughts match the provided completion ids and text
        completion_thought_ids_joined = torch.cat(completion_thoughts_ids)
        if not completion_thought_ids_joined.equal(torch.tensor(ids)):
            raise ValueError("Mismatch between provided and computed completion ids")
        thoughts_joined = "".join(completion_thoughts)

        # Completions don't include the EOS token, so remove it if we added it
        if thoughts_joined.endswith(tokenizer.eos_token):
            thoughts_joined = thoughts_joined[:-len(tokenizer.eos_token)]
        if thoughts_joined != completion:
            raise ValueError("Mismatch between provided and computed completion text")
        
        thoughts.append(completion_thoughts)
        thoughts_ids.append(completion_thoughts_ids)

    return thoughts_ids

def tokenize_answers(
    answers: list[str],
    tokenizer: PreTrainedTokenizerFast,
):
    answer_open = "<answer>" 
    answer_close = "</answer>"
    tokenized_answers = []
    for answer in answers:
        answer = answer_open + answer + answer_close
        tokenized_answers.append(
            tokenizer(text=answer, return_tensors="pt").input_ids[0]
        )
    return tokenized_answers


def tokenize_inputs(
    tokenizer: PreTrainedTokenizerFast, 
    prompts: list[str], 
    completions: list[str], 
    completion_ids: list[list[int]],
    answers: list[str],
) -> dict[str, Union[torch.Tensor, Any]]:

    prompt_inputs: BatchEncoding = tokenizer(
        text=prompts, 
        return_tensors="pt", 
        padding=True, 
        padding_side="left", 
        add_special_tokens=False
    )

    thought_ids: list[list[torch.Tensor]] = tokenize_thoughts(
        completions=completions,
        tokenizer=tokenizer,
        completion_ids=completion_ids,
    )

    answer_ids: list[torch.Tensor] = tokenize_answers(
        answers=answers,
        tokenizer=tokenizer,
    )

    return {
        PROMPT_IDS: prompt_inputs.input_ids,
        PROMPT_MASK: prompt_inputs.attention_mask,
        THOUGHT_IDS: thought_ids,
        ANSWER_IDS: answer_ids,
    }

@torch.no_grad()
def get_per_token_logps(
        model: torch.nn.Module, 
        input_ids: torch.Tensor, 
        attention_mask: torch.Tensor, 
        logits_to_keep: int,
        batch_size: int=None,
        temperature: float=1.0,
    ) -> torch.Tensor:
    batch_size = batch_size or input_ids.size(0)  # Chunk inputs into smaller batches to reduce memory peak
    all_logps = []
    for i in range(0, input_ids.size(0), batch_size):
        input_ids_batch = input_ids[i : i + batch_size]
        attention_mask_batch = attention_mask[i : i + batch_size]

        # We add 1 to `logits_to_keep` because the last logits of the sequence is later excluded
        logits = model(
            input_ids=input_ids_batch, attention_mask=attention_mask_batch, logits_to_keep=logits_to_keep + 1
        ).logits
        logits = logits[:, :-1, :]  # (B, L-1, V), exclude the last logit: it corresponds to the next token pred
        input_ids_batch = input_ids_batch[:, -logits_to_keep:]
        # Divide logits by sampling temperature.
        # See https://huggingface.co/blog/the_n_implementation_details_of_rlhf_with_ppo#policy-training-implementation-details
        logits = logits / temperature  # TODO
        logps = selective_log_softmax(logits, input_ids_batch)  # compute logprobs for the input tokens
        all_logps.append(logps)
    return torch.cat(all_logps, dim=0)

def pad_and_mask(
    sequences: list[torch.Tensor],
    tokenizer: PreTrainedTokenizerFast
):
    padded_sequences = pad_sequence(
        sequences=sequences,
        batch_first=True,
        padding_value=tokenizer.pad_token_id,
    )
    mask = (padded_sequences != tokenizer.pad_token_id).int()
    return padded_sequences, mask

def compute_CoT_rewards(
    prompts: list[str],
    completions: list[str],
    answers: list[str],
    completion_ids: list[list[int]],
    model: torch.nn.Module,
    tokenizer: PreTrainedTokenizerFast,
    device: torch.device, 
    verbose: bool=False,
):

    # Tokenize prompts and answers; partition completions into thoughts and tokenize
    input_ids = tokenize_inputs(
        tokenizer=tokenizer,
        prompts=prompts,
        completions=completions,
        completion_ids=completion_ids,
        answers=answers,
    )
    prompt_ids: torch.Tensor = input_ids[PROMPT_IDS]
    prompt_mask: torch.Tensor = input_ids[PROMPT_MASK]
    thought_ids_list: list[list[torch.Tensor]] = input_ids[THOUGHT_IDS]
    answer_ids_list: list[torch.Tensor] = input_ids[ANSWER_IDS]

    # Pad answers to the same length
    answer_ids, answer_mask = pad_and_mask(
        sequences=answer_ids_list,
        tokenizer=tokenizer,
    )
    logits_to_keep = answer_ids.shape[1]
    assert (prompt_ids != tokenizer.pad_token_id).equal(prompt_mask)

    # Evaluate the probability of the answer at each point in the chain of thought 
    per_token_answer_ps_list = []
    avg_answer_ps_list = []
    thought_end_indices = [[] for _ in range(len(thought_ids_list))]
    batch_size = len(answer_ids)
    num_thoughts = [len(t) for t in thought_ids_list]
    max_num_thoughts = max(num_thoughts)
    for thought_idx in tqdm(range(max_num_thoughts + 1)):
 
        # The first iteration (thought_idx == 0) corresponds to no CoT
        if thought_idx == 0:
            thought_ids = torch.Tensor(batch_size, 0).int()
            thought_mask = torch.Tensor(batch_size, 0).int()
        else:
            thought_ids = []
            for batch_idx in range(batch_size):
                curr_thought_list = thought_ids_list[batch_idx]
                curr_thought = torch.cat(curr_thought_list[:thought_idx])
                thought_ids.append(curr_thought)

                # Track the end index of each thought for reward assignment later
                if thought_idx <= len(curr_thought_list):
                    thought_end_indices[batch_idx].append(len(curr_thought) - 1)
            thought_ids, thought_mask = pad_and_mask(
                sequences=thought_ids,
                tokenizer=tokenizer,
            )

        # Compute probability of answer given the first `thought_idx` thoughts
        input_ids = torch.cat([prompt_ids, thought_ids, answer_ids], dim=1).to(device)
        attention_mask = torch.cat([prompt_mask, thought_mask, answer_mask], dim=1).to(device)
        per_token_answer_logps = get_per_token_logps(
            model=model, 
            input_ids=input_ids, 
            attention_mask=attention_mask, 
            logits_to_keep=logits_to_keep,
        )

        # Average the probability of each token in the answer
        per_token_answer_ps = per_token_answer_logps.exp().cpu()
        avg_answer_ps = (per_token_answer_ps * answer_mask).sum(dim=1) / answer_mask.sum(dim=1)
        per_token_answer_ps_list.append(per_token_answer_ps)
        avg_answer_ps_list.append(avg_answer_ps)

        # print_idx = -1
        # print("-" * 40 + f" thought {thought_idx} " + "-" * 40)
        # print(thought_idx)
        # print(tokenizer.decode(torch.cat([thought_ids[print_idx], answer_ids[print_idx]]), skip_special_tokens=True))
        # for p, id_ in zip(per_token_answer_ps[print_idx], answer_ids[print_idx]):
        #     print(f"{p:.3f} {tokenizer.decode(id_.unsqueeze(0))}")
        # logits_to_keep = input_ids.shape[1] - 1
        # per_token_logps_full = get_per_token_logps(
        #     model=model, 
        #     input_ids=input_ids, 
        #     attention_mask=attention_mask, 
        #     logits_to_keep=logits_to_keep,
        # )
        # assert per_token_logps_full[:, -answer_ids.shape[1]:].equal(per_token_logps)

    # Compute the increase in answer probability at each thought step
    avg_answer_ps = torch.stack(avg_answer_ps_list, dim=1)
    delta_avg_answer_ps = avg_answer_ps[:, 1:] - avg_answer_ps[:, :-1]

    # Assign rewards at the end of each thought
    linewidth=80
    reward_tensor = torch.zeros(thought_ids.shape)
    for batch_idx in range(batch_size):
        end_indices = thought_end_indices[batch_idx]
        delta_prob = delta_avg_answer_ps[batch_idx]
        if verbose:
            curr_thought_ids = thought_ids[batch_idx]
            curr_prompt_ids = prompt_ids[batch_idx]
            curr_answer_ids = answer_ids[batch_idx]
            curr_prompt_text = tokenizer.decode(curr_prompt_ids, skip_special_tokens=True).strip()
            curr_answer_text = tokenizer.decode(curr_answer_ids, skip_special_tokens=True).strip()
            print("-" * 40 + f" batch {batch_idx} " + "-" * 40)
            print()
            print(f"Prompt: {curr_prompt_text}")
            print()
            print(f"Answer: {curr_answer_text}")
        for i, end_idx in enumerate(end_indices):
            reward_tensor[batch_idx, end_idx] = delta_prob[i]
            if verbose:
                start_idx = 0 if i == 0 else end_indices[i - 1] + 1
                curr_thought_tokens = curr_thought_ids[start_idx:end_idx + 1]
                curr_thought_text = tokenizer.decode(curr_thought_tokens, skip_special_tokens=True).strip()
                print()
                print(f'Thought: "{textwrap.fill(curr_thought_text, width=linewidth)}"')
                print(f'Reward: {reward_tensor[batch_idx, end_idx]:.4f}')
    return reward_tensor

# %%

for i, ids in enumerate(reward_inputs['completion_ids'][13:]):
    thoughts, thought_ids_list = split_thoughts(
        completion_ids=ids,
        tokenizer=tokenizer,
        verbose=True
    )

# %%
device = torch.device("cuda:5")
model.to(device)
# %%

reward_tensor = compute_CoT_rewards(
    prompts=reward_inputs['prompts'],
    completions=reward_inputs['completions'],
    answers=reward_inputs['expression'],
    completion_ids=reward_inputs['completion_ids'],
    model=model,
    tokenizer=tokenizer,
    device=device,
    verbose=True,
)
# %%

# %%

reward_inputs = {
    'prompts': ['<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [70, 72, 80, 23], create an equation that equals 59. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>',
             '<|im_start|>system\n'
             'You are a helpful assistant. You first thinks about the reasoning process in the mind and then provides the user with the answer.\n'
             '<|im_end|>\n'
             '<|im_start|>user\n'
             'Using the numbers [56, 68, 85, 18], create an equation that equals 57. You can use basic arithmetic operations (+, -, *, /) and each number can '
             'only be used once. Show your work in <think> </think> tags. And return the final answer in <answer> </answer> tags, for example <answer> (1 + 2) '
             '/ 3 </answer>.<|im_end|>\n'
             '<|im_start|>assistant\n'
             'Let me solve this step by step.\n'
             '<think>'],
 'completions': [' We need to create an equation using the numbers 70, 72, 80, and 23 exactly once each, which equals 59. We have the basic arithmetic '
                 'operations: addition (+), subtraction (-), multiplication (*), and division (/). We need to be careful about the order of operations. We '
                 'should consider how we can manipulate these numbers.\n'
                 '\n'
                 "First, let's consider that 23 is a bit of a special number since it's small and can be used to adjust our target number, 59. We should "
                 'examine subtraction as a potential way to reach 59 or near it.\n'
                 '\n'
                 "Let's take away 23 from 80:\n"
                 '80 - 23 = 57\n'
                 '\n'
                 "Now our target has dropped down to 59 - 57 = 2. We need to find a way to get 2 from 72 and 70. Let's consider division:\n"
                 '72 / 36 = 2\n'
                 '\n'
                 "Assuming 70 / 35 = 2 isn't allowed, we need to use 70 in our equation. But 70 ÷ 3.5 isn't available since it could not be simplified further "
                 'while using the numbers as whole. Thus, we use a valid division operation:\n'
                 '70 / 35 = 2\n'
                 '\n'
                 'So now our equation includes:\n'
                 '80 - 23 - (70 / 35) = 59\n'
                 '\n'
                 'Notice that the division (70 / 35) within the parentheses simplifies to 2. </think>\n'
                 '<answer> 80 - 23 - (70 / 35) </answer>',
                 " We need to use each of the numbers 70, 72, 80, and 23 exactly once to get a result of 59. Each operation can only be used once. Let's start "
                 'by calculating sums and differences between these numbers to see if we can get close to 59.\n'
                 "Considering subtraction: If we use 80 - 72, we get 8. But this doesn't help directly as we need the result to be 59.\n"
                 'Considering addition, if we try 70 + 72 - 80 - 23, we calculate it as follows:\n'
                 '70 + 72 = 142\n'
                 '142 - 80 = 62\n'
                 '62 - 23 = 39\n'
                 'We now have 39, but we need 59. This means our initial subtraction needs adjustment, since subtraction will keep us lower than we need.\n'
                 "Let's also consider multiplication and division. 70/80 = 0.875, 80/70 = a bit less than 1, 72/23 = 3.13, 23/70 = a bit less than 0.3. None "
                 'of these produce a result close to 59, as they are either too small or too large.</think>\n'
                 "In <think> </think> tags, I've tried calculation options but could not find a combination of basic arithmetic operations that apply to all "
                 'numbers exactly once to yield 59 directly. However, I can still find a pattern or combination that suits the equation. Let me revisit using '
                 'a different perspective after exploiting the arithmetic operations more effectively.\n'
                 'My next idea is to directly resolve the arithmetic in a different order. Instead of trial and error, we should focus on manipulating the '
                 "numbers in a cogited cycle. Let's try:\n"
                 '(72 - 70) * 23 / 80\n'
                 'This results in:\n'
                 '(2) * 23 / 80\n'
                 '46 / 80\n'
                 '0.575\n'
                 'Again, not right. Perhaps my interopration was flawed. \n'
                 '(Thought here for possible misuse in angles) This operation still does not yield 59. \n'
                 "Aha! Let's envision using the modulo operation to adjust the result. \n"
                 "Let's attempt this augmented:\n"
                 '(23 % 80) / (72 - 70)\n'
                 'Numbers ',
                 ' Given numbers: 70, 72, 80, and 23.\n'
                 'We need to form an equation that equals 59 using each number exactly once and only using the operations of addition, subtraction, '
                 'multiplication, and division once.\n'
                 '\n'
                 "Let's start with the larger numbers to see what we can do initially. Dividing 80 by 23 seems reasonable, as it will give us a number close "
                 'to 3.\n'
                 '\n'
                 '80 / 23 = 3.4782608695...\n'
                 '\n'
                 'From this, the closest integer is 3. If we subtract this from 23, we get:\n'
                 '23 - 3 = 20.\n'
                 '\n'
                 "Now, let's divide 72 by 3:\n"
                 '72 / 3 = 24.\n'
                 '\n'
                 'Our goal is 59. If we add 24 and 34, we get:\n'
                 '24 + 34 = 58.\n'
                 '\n'
                 'We need one more unit to reach 59. Notice that if we subtract:\n'
                 '23 - 3 - 30 = 0\n'
                 '\n'
                 'We see that using the 70 and subtracting 30 will work:\n'
                 '23 - 3 - 30 = -10.\n'
                 '\n'
                 'But we need to add to get to 59, not subtract. So we take another look at simplifying the 23, 24 -> 24 + 3 = 27, and adding subtraction '
                 'using the 70:\n'
                 '70 - 23 = 47, this is close to 34 to get to 59, when adding:\n'
                 '\n'
                 '24 + 3 + 47 - 16 = 59.\n'
                 '\n'
                 'But the terms -30 and 16 introduce complications. Using simpler, conservative operations, we realize:\n'
                 '70 - 23 = 47, and completing 24 + 3 = 27:\n'
                 '27 + 32 = 59 is inefficient.\n'
                 '\n'
                 'Upon re-examination, 24 + 70 - 23 = 71; subtracting 2 so we match 59:\n'
                 '72 - 3 = 69, giving 58, and 1 reduces:\n'
                 '69 - 1 = 68, close:\n'
                 '\n'
                 '69 - 1 = 59.\n'
                 '\n'
                 'That is simple operationally: </think>\n'
                 '<answer> 72 - 23 + 1',
                 ' I need to manipulate the numbers 70, 72, 80, and 23 using basic arithmetic operations so that the result is 59. \n'
                 'The key numbers are 80 and 23, as they are quite far from 59. A subtraction from 80 could help. If I subtract 23 from 80, I get 57. From '
                 "there, I'll need to adjust it to 59, which means an addition of 2. \n"
                 'So, 80 - 23 equals 57. To get to 59, I need 2. The numbers 23 and 72 have 23, so I can use 72 - 23 = 49 and then add 2 to 49 to get 59. \n'
                 'That means I can use these operations on 72, 23, and the final subtraction from 80 to get to 59.\n'
                 '</think>\n'
                 '<answer> (72 - 23) + (80 - 70) </answer>',
                 ' We have to use the numbers 70, 72, 80, and 23 exactly once to get 59.\n'
                 'One approach is to start by looking at the target number and think about how to use the highest and lowest numbers available to most quickly '
                 'reach or get close to the target.\n'
                 "72 - 80 gives -8, which is a big negative number and far from 59. We can't use subtraction alone.\n"
                 "Perhaps we can multiply or add one of the numbers. 70 could be a strong base but it's too high.\n"
                 'Dividing might help. 23 * 2 = 46 is manageable, and subtracting that reduces the value more effectively.\n'
                 "Then 80 - 23 = 57, and 57 - 46 = 11. We're close but not close enough.\n"
                 'Another approach is to start with 72 and subtracting 23 to get something close, then multiply by 0.2 (0.2 * 57) so we adjust the value.\n'
                 "Let's break it down:\n"
                 '80 - 23 = 57\n'
                 'Then 57 / 10 = 5.7 (round it to 5 as per available simple operations)\n'
                 'We need to get from 5.7 to 59. Multiplying 5.7 by 11 gives us 62.7 which is close to 59.\n'
                 "However, we don't have 11 in our number set. We need to interpolate. \n"
                 '57 * 0.9 = 51.3, close but not enough,\n'
                 '57 * 1.1 = 62.7 too much.\n'
                 '\n'
                 'Given our constrained numbers, a clever combination: \n'
                 '(80 - 70) * 72 / 23 + 72/70 = 59\n'
                 '\n'
                 "Let's check the equation: \n"
                 '- First (80 - 70) = 10\n'
                 '- Then 10 * 72 = 720\n'
                 '- Then 720 / 23 ≈ 31.3\n'
                 '- 72/70 ≈ 1.03\n'
                 '- Add them together:\n'
                 '720 / 23 + 72/70 ≈ 31.3 + 1.03 = 32.33\n'
                 'This is not 5',
                 ' We have the numbers 70, 72, 80, 23. We need to create an equation using these numbers exactly once, to achieve a result of 59.\n'
                 'One effective way to think about this is to try to use operations that can lead to subtraction or a round number around 59.\n'
                 'If we attempt to use the largest numbers first and then modify their outcomes with smaller numbers, we might get closer to the target. \n'
                 'Considering 72 and 23 especially, we might subtract 23 from 72 to get 49. But we need to adjust to reach 59. Adding 10 to 49 does the '
                 'trick.\n'
                 'So, the equation would look something like (72 - 23) + X = 59.\n'
                 'Simplifying (72 - 23) we have 49, so (49 + X) = 59.\n'
                 'That means X = 59 - 49, which is 10.\n'
                 'Now we know we need 10, and we have the remaining number 70. We need to use it to create 10.\n'
                 "Let's see how... If we divide 70 by 7, we get 10.\n"
                 'So the equation works out to be: 70 / 7 + 72 - 23 = 59.\n'
                 '</think>\n'
                 '<answer> 70 / 7 + 72 - 23 </answer>',
                 " Since we are looking for an equation that results in 59, and we're limited to using each number [70, 72, 80, 23] only once, the goal is to "
                 'manipulate these numbers through basic arithmetic operations. One possible way to approach this is to start with some straightforward '
                 "calculations and see if we can arrive at 59. Let's consider the known numbers and try combining them in different ways. Maybe the difference "
                 "between some numbers will yield something close to 59. Let's try 80 - 23 to get 57, then see if manipulating 70 and 72 will reach 59. "
                 '</think>\n'
                 'We have 80 - 23 = 57. We need to end up with 59. Now, we need to adjust 57 to get to 59. One way to do this is by using 72 - 70 = 2. Then '
                 'adding this 2 to 57 will give 59. \n'
                 "Let's formulate this:\n"
                 '<answer> (80 - 23) + (72 - 70) </answer>',
                 ' We have four given numbers: 70, 72, 80, and 23. Our goal is to use each number exactly once and employ basic arithmetic operations to reach '
                 'the result of 59. \n'
                 '\n'
                 'If we look at the given numbers, first considering the equation structure, it seems unlikely that simple addition or subtraction could lead '
                 'us to 59 due to the gap still remaining in such operations with the numbers given. So, we need to think of more complex operations using '
                 'multiplication and division, because they can help reduce the numbers more efficiently.\n'
                 '\n'
                 "Let's consider the calculation step-by-step by adding and subtracting one set of numbers, then using division to get as close as possible to "
                 "59. Let's try:\n"
                 '(72 + 80) / 70 = 152 / 70 which is slightly more than 2.\n'
                 'Next, subtract 23:\n'
                 '152 / 70 - 23 = 2.1714 - 23 which is too small.\n'
                 'What seems more strategic could be:\n'
                 '72 + 23 - (80 / 70) = 95 - 1.1429 = 93.8571 which is still not correct.\n'
                 '\n'
                 "Let's try another combination:\n"
                 '72 + 70 - 80 - 23 = 69 - 23 = 46. Now, we need to reduce it to 59, we need to use multiplication next, thus we recognize:\n'
                 '72 * (80 / 23) = 72 * 3.4783 = 249.7896 which is very close but not 59; the remaining operation should be a subtweighted subtraction or '
                 'addition. </think>\n'
                 '\n'
                 'Now, after considering, the equation must be:\n'
                 '<answer> 72 - 23 + 70 / 80 </answer>\n'
                 '</answer>\n'
                 '\n'
                 "Let's plug it back for checking:\n"
                 '<think> 72 - 23 + 70 / 80 = 49 + 0.875 = 59.875. </think>\n'
                 '\n'
                 "Upon a closer look at this, it's not precisely 59, but given the constraints of using all numbers once and available operations, the closest "
                 'is probably <answer> 72 - 23 + 70 / 80 </',
                 " I need to create an equation using the numbers 56, 68, 85, and 18 that results in 57. I can utilize each number only once. Let's start by "
                 'considering if plugging numbers directly or reducing them through arithmetic operations will lead to the right result.\n'
                 'If I divide 18 by 3, that results in 6. Right after that, I could potentially subtract or add some numbers to get closer to my target of 57. '
                 'I also consider addition between some of the larger numbers.</think>\n'
                 'Based on careful consideration, the equation that uses each of the numbers exactly once and equals 57 should be:\n'
                 '<answer> 85 - 68 + 56 / 18 </answer>\n'
                 '</think>\n'
                 'Let me break it down to verify:\n'
                 '- 56 / 18 = 3.111...\n'
                 '- 68 - 3.111... = 64.888...\n'
                 '- 85 - 64.888... = 20.111...\n'
                 '- 20.111... + 56 / 18 = 57\n'
                 "It seems the operation flagged is slightly incorrect due to rounding. Let's do a quick check:\n"
                 '- 56 / 18 = 3.111... (exact decimal division)\n'
                 '- 68 - 3.111... = 64.888...\n'
                 '- 85 - 64.888... = 20.111...\n'
                 '- 20.111... + 3.111... = 53.222...\n'
                 "This still doesn't reach 57. Let's adjust the way we use the numbers. Revisiting the idea of addition might be better:\n"
                 '<answer> 68 + (85 - 56 - 18 / 2) </answer>\n'
                 '</think>\n'
                 '</think>\n'
                 'Let me confirm the revised equation:\n'
                 '- 18 / 2 = 9\n'
                 '- 85 - 56 - 9 = 20\n'
                 '- 68 + 20 = 88\n'
                 '\n'
                 'The equation 68 + (85 - 56 - 18 / 2) correctly uses all the numbers exactly once and equals 88.\n'
                 'Since the original target of 57 cannot',
                 'Firstly, 57 is very close to 56 and 68 which are both given numbers. One way to get to 57 is by adding or subtracting a number by 1. Knowing '
                 'that all numbers can only be used once, 18 can be the number by which to subtract 56 to get 57. But the numbers are 56, 68, 85, and 18, none '
                 "of which are 1, and subtracting 18 from 56 won't lead us to 68 or 85. So, that doesn't work.</think>\n"
                 'A different approach might explore dividing operations since dividing can help balance the equation using the higher numbers (68 and 85). '
                 "Sixty-eight divided by 1.5 can potentially give us 45.33... or 57 with rounding or approximate means. But 1.5 isn't an integer. However, it "
                 'offers insight that division especially with 18 as a factor may be possible.\n'
                 'Consider the numbers 68, 18, and 85. If 68 divided by 1.5 equals 45 and we subtract 18 from it, we might approach 57. However, 18 divided by '
                 '1.5 equals 12, so 68 - 12 = 56, and 56 + 1 = 57.\n'
                 "This gives us three numbers to work with: 68, 18, and 1. And the fourth is left as we set initially. For this equation, let's reframe using "
                 'basic arithmetic operations.\n'
                 '</think>\n'
                 '<answer> (68 - 18 + 1) / 1 </answer>\n'
                 'This equation translates to: ((68 - 18) + 1) / 1, which simplifies to 56 + 1, which equals 57. Since all operations should be performed in '
                 'the order they appear, this gives us the final answer: (57 / 1) = 57.',
                 'Firstly, 57 can be expressed as 50 + 7, so one of the combinations would involve this. One simple way is to express 50 as a combination of '
                 'the numbers 56, 68, and 18, and then combine it with 7 using the operations available. Now, 56 - 18 = 38 and 68 - 18 = 50, so we can combine '
                 "these to make 38 + 50. We now need 7, which could have been the third number left over as a whole or as part of another number. Let's try to "
                 'fit 56 as 38 + 18 and then add 7, as 38 + 18 + 7 = 63, which simplifies to 50 + 7 when 18 is subtracted.</think>\n'
                 '<answer>(56 - 18) + (68 - 18 - 7)</answer>',
                 ' I need to form an equation using the numbers 56, 68, 85, and 18, with all operations being basic arithmetic, and each digit used exactly '
                 'once. The target number is 57. </think>\n'
                 'Considering the target number 57, it seems close to the number 56. I can subtract 1 from 56, which would give me 57. \n'
                 "Using the number 18, I can subtract 18 from 56, but that would result in 38, not 57. Instead, I'll see if I can use division or other "
                 'manipulations. </think>\n'
                 'I realize I can divide 56 by 9 (which uses 56 and leaves me with 9 on the other side), and if I subtract or add 9 appropriately, I can get '
                 "close to 57. Actually, dividing by 9 may yield a decimal, which isn't ideal. Subtracting or adding 18 from 56 or 85 might not work given the "
                 "format I'm looking for.\n"
                 "Let's try another approach. If I consider the equation in a more creative way, I might think about adding or subtracting smaller numbers to "
                 '56. Since 18 could be an opponent, I might need to offset it somehow.\n'
                 "I'll test the equation: (68 - 85) / 18 + 56.\n"
                 '</think>\n'
                 'Now, let me calculate this equation.\n'
                 '<answer> (68 - 85) / 18 + 56 </answer> = -17 / 18 + 56.\n'
                 "Let's evaluate this: -17 / 18 = -0.9444...\n"
                 '-0.9444... + 56 = 55.0556...\n'
                 'The result is not exactly 57, which suggests I need to re-evaluate the numbers and operations.\n'
                 "After further consideration, I realize I need to carefully account for all possible operations and combinations. Let's try another "
                 'approach.\n'
                 '(think) Re-evaluating, I realize that if I use the number 68 to help reach our target, I can look for a proper way to use 56, 85, and 18 to '
                 'offset and reach 57. </think>\n'
                 'A possible mix could be using addition or multiplication creatively to hold the final sum.\n'
                 '\n'
                 'So, let me test',
                 "Firstly, I notice that 57 is close to the sum of 68 and 18, which gives 86. That's above 57. Subtracting 29 from 86 would get us close to "
                 '57, and 29 happens to be the sum of 56 - 28 = 56 - 85 + 18. Therefore, I can use these numbers to form an equation. We can start with 68 - '
                 '(56 - 85 + 18) and subtract 29.</think>\n'
                 '<answer> 68 - (56 - 85 + 18) - 29 </answer>',
                 "First, I will see if I can use the numbers directly to get close to 57. Oftentimes with these equations, such a simple strategy works. I'll "
                 'try to reach a number close to 57 by combining two of the numbers. The numbers 56 and 18 add up to 74, which is too high. 68 and 85 sum to '
                 '153, which is also too high. </think>\n'
                 '\n'
                 "Next, I notice that 68 - 18 = 50, which is close to 57. Then, I'll use division and subtraction to make a fine adjustment. \n"
                 '<answer>(68 - 18) / 56 + 85 - 68 = 57</answer> \n'
                 '\n'
                 'However, on calculation, this results in:\n'
                 '<answer>50 / 56 + 85 - 68 = 4.2857 + 85 - 68 ≈ 21.2857 <answer>\n'
                 '\n'
                 "This doesn't result in 57, so I need to rethink my approach. Let's try 85 - 68 = 17. Then, I can add 18 and subtract 56 to get close to 57.\n"
                 '<answer>(85 - 68) + 18 - 56 = 57</answer>\n'
                 '\n'
                 "Now, let's verify this equation.\n"
                 '</think>\n'
                 '<answer>(85 - 68) + 18 - 56 = 57</answer>',
                 "Firstly, the target number is 57. Looking at the list, the number 56 stands out as 57 - 1 from our list. Let's check if 56 and 1 can be "
                 'derived from the others using the available operations (+, -, *, /).</think>\n'
                 'We can express 57 - 56 as 1, but the challenge is to generate 1 using the remaining numbers and operators.\n'
                 'Considering the number 18, dividing it by 68 could give us a substantial value, and subtracting a portion of that from 68 or 85 could help '
                 'in achieving 57.\n'
                 "Handling the division of 18 by 68, we get 18/68 = 0.2647 when approximated, which isn't precise for our target of 1. However, we likely can "
                 'scale this to get our desired value by manipulating the operations and the numbers provided once.\n'
                 '</think>\n'
                 'Now the idea is clear:\n'
                 '<answer> (85 - 68) / 18 * 1 + 56 </answer> which simplifies to <answer> 17/18 * 1 + 56 </answer>\n'
                 'To reach 57:\n'
                 '<answer> = (17/18) * 18 + 56 = 17 + 56 = 57 </answer>\n'
                 '\n'
                 'Thus, the expression correctly uses the numbers [56, 68, 85, 18] and the operations to equal 57.',
                 ' I need to use the numbers 56, 68, 85, and 18 exactly once to get a result of 57. I should note that division can work with integers to '
                 "yield whole numbers, but I'll also consider other operations.</think>\n"
                 'Considering integer division and basic operations like addition, subtraction, multiplication, and division with whole numbers. Let me check '
                 'different combinations:\n'
                 '<answer> (85 + 18 - 68) / 56 </answer>\n'
                 "I'll verify this:\n"
                 '1. Start with the expression: (85 + 18 - 68) / 56\n'
                 '2. Calculate the sum: 85 + 18 = 103\n'
                 '3. Subtract 68 from 103: 103 - 68 = 35\n'
                 '4. Finally, divide by 56: 35 / 56 = 0.625\n'
                 "This doesn't quite work. Let's try another combination:\n"
                 '\n'
                 '<answer> (85 - 56) + (18 / 68) </answer>\n'
                 "I'll verify:\n"
                 '1. Start with the expression: (85 - 56) + (18 / 68)\n'
                 '2. Difference between 85 and 56: 85 - 56 = 29\n'
                 '3. Division 18 / 68 is approximately 0.2647 (using a calculator)\n'
                 '4. Sum of 29 and 0.2647 is approximately 29.2647\n'
                 "This isn't 57 either, but it's close enough in absolute terms. Since I need an exact solution, let's try another combination:\n"
                 '\n'
                 '<answer> (85 - 68) + 56 / 18 </answer>\n'
                 "I'll verify:\n"
                 '1. Start with the expression: (85 - 68) + 56 / 18\n'
                 '2. Difference 85 - 68 = 17\n'
                 '3. Division 56 / 18 is approximately 3.1111\n'
                 '4. Adding 17 and 3.1111 = 20.1111\n'
                 "Still not equal to 57. Let's try one more combination:\n"
                 '\n'
                 '<answer> (56 * 85 - 68 - 18)'],
 'expression': ['(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)',
                '(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)', '(((72 - 23) + 80) - 70)', '(((68 + 18) + 56) - 85)', '(((68 + 18) + 56) - 85)',
                '(((68 + 18) + 56) - 85)', '(((68 + 18) + 56) - 85)', '(((68 + 18) + 56) - 85)', '(((68 + 18) + 56) - 85)', '(((68 + 18) + 56) - 85)',
                '(((68 + 18) + 56) - 85)'],
 'completion_ids': [[1205, 1184, 311, 1855, 458, 23606, 1667, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 6896, 3055, 1817,
                     11, 892, 16819, 220, 20, 24, 13, 1205, 614, 279, 6770, 34784, 7525, 25, 5256, 17973, 701, 75240, 10293, 701, 46444, 4609, 701, 323, 12804,
                     46225, 568, 1205, 1184, 311, 387, 16585, 911, 279, 1973, 315, 7525, 13, 1205, 1265, 2908, 1246, 582, 646, 36635, 1493, 5109, 382, 5338, 11,
                     1077, 594, 2908, 429, 220, 17, 18, 374, 264, 2699, 315, 264, 3281, 1372, 2474, 432, 594, 2613, 323, 646, 387, 1483, 311, 7500, 1039, 2169,
                     1372, 11, 220, 20, 24, 13, 1205, 1265, 20961, 75240, 438, 264, 4650, 1616, 311, 5545, 220, 20, 24, 476, 3143, 432, 382, 10061, 594, 1896,
                     3123, 220, 17, 18, 504, 220, 23, 15, 510, 23, 15, 481, 220, 17, 18, 284, 220, 20, 22, 271, 7039, 1039, 2169, 702, 12226, 1495, 311, 220,
                     20, 24, 481, 220, 20, 22, 284, 220, 17, 13, 1205, 1184, 311, 1477, 264, 1616, 311, 633, 220, 17, 504, 220, 22, 17, 323, 220, 22, 15, 13,
                     6771, 594, 2908, 12804, 510, 22, 17, 608, 220, 18, 21, 284, 220, 17, 271, 5615, 29489, 220, 22, 15, 608, 220, 18, 20, 284, 220, 17, 4436,
                     944, 5420, 11, 582, 1184, 311, 990, 220, 22, 15, 304, 1039, 23606, 13, 1988, 220, 22, 15, 1683, 115, 220, 18, 13, 20, 4436, 944, 2500,
                     2474, 432, 1410, 537, 387, 43799, 4623, 1393, 1667, 279, 5109, 438, 4361, 13, 14301, 11, 582, 990, 264, 2697, 12804, 5666, 510, 22, 15,
                     608, 220, 18, 20, 284, 220, 17, 271, 4416, 1431, 1039, 23606, 5646, 510, 23, 15, 481, 220, 17, 18, 481, 320, 22, 15, 608, 220, 18, 20, 8,
                     284, 220, 20, 24, 271, 34193, 429, 279, 12804, 320, 22, 15, 608, 220, 18, 20, 8, 2878, 279, 73975, 15491, 9606, 311, 220, 17, 13, 690,
                     26865, 397, 27, 9217, 29, 220, 23, 15, 481, 220, 17, 18, 481, 320, 22, 15, 608, 220, 18, 20, 8, 690, 9217, 29, 151645],
                    [1205, 1184, 311, 990, 1817, 315, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 6896, 3055, 311, 633, 264,
                     1102, 315, 220, 20, 24, 13, 8886, 5666, 646, 1172, 387, 1483, 3055, 13, 6771, 594, 1191, 553, 37614, 36398, 323, 11799, 1948, 1493, 5109,
                     311, 1490, 421, 582, 646, 633, 3265, 311, 220, 20, 24, 624, 82796, 75240, 25, 1416, 582, 990, 220, 23, 15, 481, 220, 22, 17, 11, 582, 633,
                     220, 23, 13, 1988, 419, 3171, 944, 1492, 5961, 438, 582, 1184, 279, 1102, 311, 387, 220, 20, 24, 624, 82796, 5256, 11, 421, 582, 1430, 220,
                     22, 15, 488, 220, 22, 17, 481, 220, 23, 15, 481, 220, 17, 18, 11, 582, 11047, 432, 438, 11017, 510, 22, 15, 488, 220, 22, 17, 284, 220, 16,
                     19, 17, 198, 16, 19, 17, 481, 220, 23, 15, 284, 220, 21, 17, 198, 21, 17, 481, 220, 17, 18, 284, 220, 18, 24, 198, 1654, 1431, 614, 220,
                     18, 24, 11, 714, 582, 1184, 220, 20, 24, 13, 1096, 3363, 1039, 2856, 75240, 3880, 27075, 11, 2474, 75240, 686, 2506, 601, 4722, 1091, 582,
                     1184, 624, 10061, 594, 1083, 2908, 46444, 323, 12804, 13, 220, 22, 15, 14, 23, 15, 284, 220, 15, 13, 23, 22, 20, 11, 220, 23, 15, 14, 22,
                     15, 284, 264, 2699, 2686, 1091, 220, 16, 11, 220, 22, 17, 14, 17, 18, 284, 220, 18, 13, 16, 18, 11, 220, 17, 18, 14, 22, 15, 284, 264,
                     2699, 2686, 1091, 220, 15, 13, 18, 13, 2240, 315, 1493, 8193, 264, 1102, 3265, 311, 220, 20, 24, 11, 438, 807, 525, 2987, 2238, 2613, 476,
                     2238, 3460, 3918, 26865, 397, 641, 366, 26865, 29, 690, 26865, 29, 9492, 11, 358, 3003, 6679, 21937, 2606, 714, 1410, 537, 1477, 264,
                     10601, 315, 6770, 34784, 7525, 429, 3796, 311, 678, 5109, 6896, 3055, 311, 7540, 220, 20, 24, 5961, 13, 4354, 11, 358, 646, 2058, 1477,
                     264, 5383, 476, 10601, 429, 27976, 279, 23606, 13, 6771, 752, 64778, 1667, 264, 2155, 13057, 1283, 70601, 279, 34784, 7525, 803, 13444,
                     624, 5050, 1790, 4522, 374, 311, 5961, 8830, 279, 34784, 304, 264, 2155, 1973, 13, 12090, 315, 9091, 323, 1465, 11, 582, 1265, 5244, 389,
                     62514, 279, 5109, 304, 264, 61566, 1608, 10775, 13, 6771, 594, 1430, 510, 7, 22, 17, 481, 220, 22, 15, 8, 353, 220, 17, 18, 608, 220, 23,
                     15, 198, 1986, 3059, 304, 510, 7, 17, 8, 353, 220, 17, 18, 608, 220, 23, 15, 198, 19, 21, 608, 220, 23, 15, 198, 15, 13, 20, 22, 20, 198,
                     30385, 11, 537, 1290, 13, 18765, 847, 946, 453, 2165, 572, 46908, 13, 715, 7, 84169, 1588, 369, 3204, 61751, 304, 25941, 8, 1096, 5666,
                     2058, 1558, 537, 7540, 220, 20, 24, 13, 715, 32, 4223, 0, 6771, 594, 47046, 1667, 279, 59864, 5666, 311, 7500, 279, 1102, 13, 715, 10061,
                     594, 4774, 419, 55988, 510, 7, 17, 18, 1018, 220, 23, 15, 8, 608, 320, 22, 17, 481, 220, 22, 15, 340, 27237, 220],
                    [16246, 5109, 25, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 624, 1654, 1184, 311, 1352, 458, 23606, 429, 16819,
                     220, 20, 24, 1667, 1817, 1372, 6896, 3055, 323, 1172, 1667, 279, 7525, 315, 5256, 11, 75240, 11, 46444, 11, 323, 12804, 3055, 382, 10061,
                     594, 1191, 448, 279, 8131, 5109, 311, 1490, 1128, 582, 646, 653, 15102, 13, 8765, 6577, 220, 23, 15, 553, 220, 17, 18, 4977, 13276, 11,
                     438, 432, 686, 2968, 601, 264, 1372, 3265, 311, 220, 18, 382, 23, 15, 608, 220, 17, 18, 284, 220, 18, 13, 19, 22, 23, 17, 21, 15, 23, 21,
                     24, 20, 2146, 3830, 419, 11, 279, 18093, 7546, 374, 220, 18, 13, 1416, 582, 32256, 419, 504, 220, 17, 18, 11, 582, 633, 510, 17, 18, 481,
                     220, 18, 284, 220, 17, 15, 382, 7039, 11, 1077, 594, 21749, 220, 22, 17, 553, 220, 18, 510, 22, 17, 608, 220, 18, 284, 220, 17, 19, 382,
                     7981, 5795, 374, 220, 20, 24, 13, 1416, 582, 912, 220, 17, 19, 323, 220, 18, 19, 11, 582, 633, 510, 17, 19, 488, 220, 18, 19, 284, 220, 20,
                     23, 382, 1654, 1184, 825, 803, 4982, 311, 5545, 220, 20, 24, 13, 24742, 429, 421, 582, 32256, 510, 17, 18, 481, 220, 18, 481, 220, 18, 15,
                     284, 220, 15, 271, 1654, 1490, 429, 1667, 279, 220, 22, 15, 323, 32256, 287, 220, 18, 15, 686, 975, 510, 17, 18, 481, 220, 18, 481, 220,
                     18, 15, 284, 481, 16, 15, 382, 3983, 582, 1184, 311, 912, 311, 633, 311, 220, 20, 24, 11, 537, 32256, 13, 2055, 582, 1896, 2441, 1401, 518,
                     15491, 7766, 279, 220, 17, 18, 11, 220, 17, 19, 1464, 220, 17, 19, 488, 220, 18, 284, 220, 17, 22, 11, 323, 7842, 75240, 1667, 279, 220,
                     22, 15, 510, 22, 15, 481, 220, 17, 18, 284, 220, 19, 22, 11, 419, 374, 3265, 311, 220, 18, 19, 311, 633, 311, 220, 20, 24, 11, 979, 7842,
                     1447, 17, 19, 488, 220, 18, 488, 220, 19, 22, 481, 220, 16, 21, 284, 220, 20, 24, 382, 3983, 279, 3793, 481, 18, 15, 323, 220, 16, 21,
                     19131, 35405, 13, 12091, 34288, 11, 15332, 7525, 11, 582, 13083, 510, 22, 15, 481, 220, 17, 18, 284, 220, 19, 22, 11, 323, 26568, 220, 17,
                     19, 488, 220, 18, 284, 220, 17, 22, 510, 17, 22, 488, 220, 18, 17, 284, 220, 20, 24, 374, 63381, 382, 49284, 312, 10187, 26837, 11, 220,
                     17, 19, 488, 220, 22, 15, 481, 220, 17, 18, 284, 220, 22, 16, 26, 32256, 287, 220, 17, 773, 582, 2432, 220, 20, 24, 510, 22, 17, 481, 220,
                     18, 284, 220, 21, 24, 11, 7086, 220, 20, 23, 11, 323, 220, 16, 25271, 510, 21, 24, 481, 220, 16, 284, 220, 21, 23, 11, 3265, 1447, 21, 24,
                     481, 220, 16, 284, 220, 20, 24, 382, 4792, 374, 4285, 5666, 745, 25, 690, 26865, 397, 27, 9217, 29, 220, 22, 17, 481, 220, 17, 18, 488,
                     220, 16],
                    [358, 1184, 311, 36635, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 1667, 6770, 34784, 7525, 773, 429,
                     279, 1102, 374, 220, 20, 24, 13, 715, 785, 1376, 5109, 525, 220, 23, 15, 323, 220, 17, 18, 11, 438, 807, 525, 5008, 3041, 504, 220, 20, 24,
                     13, 362, 75240, 504, 220, 23, 15, 1410, 1492, 13, 1416, 358, 32256, 220, 17, 18, 504, 220, 23, 15, 11, 358, 633, 220, 20, 22, 13, 5542,
                     1052, 11, 358, 3278, 1184, 311, 7500, 432, 311, 220, 20, 24, 11, 892, 3363, 458, 5256, 315, 220, 17, 13, 715, 4416, 11, 220, 23, 15, 481,
                     220, 17, 18, 16819, 220, 20, 22, 13, 2014, 633, 311, 220, 20, 24, 11, 358, 1184, 220, 17, 13, 576, 5109, 220, 17, 18, 323, 220, 22, 17,
                     614, 220, 17, 18, 11, 773, 358, 646, 990, 220, 22, 17, 481, 220, 17, 18, 284, 220, 19, 24, 323, 1221, 912, 220, 17, 311, 220, 19, 24, 311,
                     633, 220, 20, 24, 13, 715, 4792, 3363, 358, 646, 990, 1493, 7525, 389, 220, 22, 17, 11, 220, 17, 18, 11, 323, 279, 1590, 75240, 504, 220,
                     23, 15, 311, 633, 311, 220, 20, 24, 624, 522, 26865, 397, 27, 9217, 29, 320, 22, 17, 481, 220, 17, 18, 8, 488, 320, 23, 15, 481, 220, 22,
                     15, 8, 690, 9217, 29, 151645],
                    [1205, 614, 311, 990, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 6896, 3055, 311, 633, 220, 20, 24,
                     624, 3966, 5486, 374, 311, 1191, 553, 3330, 518, 279, 2169, 1372, 323, 1744, 911, 1246, 311, 990, 279, 8426, 323, 15457, 5109, 2500, 311,
                     1429, 6157, 5545, 476, 633, 3265, 311, 279, 2169, 624, 22, 17, 481, 220, 23, 15, 6696, 481, 23, 11, 892, 374, 264, 2409, 8225, 1372, 323,
                     3041, 504, 220, 20, 24, 13, 1205, 646, 944, 990, 75240, 7484, 624, 31476, 582, 646, 30270, 476, 912, 825, 315, 279, 5109, 13, 220, 22, 15,
                     1410, 387, 264, 3746, 2331, 714, 432, 594, 2238, 1550, 624, 12509, 6577, 2578, 1492, 13, 220, 17, 18, 353, 220, 17, 284, 220, 19, 21, 374,
                     70028, 11, 323, 32256, 287, 429, 25271, 279, 897, 803, 13444, 624, 12209, 220, 23, 15, 481, 220, 17, 18, 284, 220, 20, 22, 11, 323, 220,
                     20, 22, 481, 220, 19, 21, 284, 220, 16, 16, 13, 1205, 2299, 3265, 714, 537, 3265, 3322, 624, 14037, 5486, 374, 311, 1191, 448, 220, 22, 17,
                     323, 32256, 287, 220, 17, 18, 311, 633, 2494, 3265, 11, 1221, 30270, 553, 220, 15, 13, 17, 320, 15, 13, 17, 353, 220, 20, 22, 8, 773, 582,
                     7500, 279, 897, 624, 10061, 594, 1438, 432, 1495, 510, 23, 15, 481, 220, 17, 18, 284, 220, 20, 22, 198, 12209, 220, 20, 22, 608, 220, 16,
                     15, 284, 220, 20, 13, 22, 320, 1049, 432, 311, 220, 20, 438, 817, 2500, 4285, 7525, 340, 1654, 1184, 311, 633, 504, 220, 20, 13, 22, 311,
                     220, 20, 24, 13, 58712, 6711, 220, 20, 13, 22, 553, 220, 16, 16, 6696, 601, 220, 21, 17, 13, 22, 892, 374, 3265, 311, 220, 20, 24, 624,
                     11209, 11, 582, 1513, 944, 614, 220, 16, 16, 304, 1039, 1372, 738, 13, 1205, 1184, 311, 59457, 13, 715, 20, 22, 353, 220, 15, 13, 24, 284,
                     220, 20, 16, 13, 18, 11, 3265, 714, 537, 3322, 345, 20, 22, 353, 220, 16, 13, 16, 284, 220, 21, 17, 13, 22, 2238, 1753, 382, 22043, 1039,
                     53752, 5109, 11, 264, 27699, 10601, 25, 715, 7, 23, 15, 481, 220, 22, 15, 8, 353, 220, 22, 17, 608, 220, 17, 18, 488, 220, 22, 17, 14, 22,
                     15, 284, 220, 20, 24, 271, 10061, 594, 1779, 279, 23606, 25, 715, 12, 5512, 320, 23, 15, 481, 220, 22, 15, 8, 284, 220, 16, 15, 198, 12,
                     5005, 220, 16, 15, 353, 220, 22, 17, 284, 220, 22, 17, 15, 198, 12, 5005, 220, 22, 17, 15, 608, 220, 17, 18, 21103, 230, 220, 18, 16, 13,
                     18, 198, 12, 220, 22, 17, 14, 22, 15, 21103, 230, 220, 16, 13, 15, 18, 198, 12, 2691, 1105, 3786, 510, 22, 17, 15, 608, 220, 17, 18, 488,
                     220, 22, 17, 14, 22, 15, 21103, 230, 220, 18, 16, 13, 18, 488, 220, 16, 13, 15, 18, 284, 220, 18, 17, 13, 18, 18, 198, 1986, 374, 537, 220,
                     20],
                    [1205, 614, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 220, 17, 18, 13, 1205, 1184, 311, 1855, 458, 23606, 1667, 1493,
                     5109, 6896, 3055, 11, 311, 11075, 264, 1102, 315, 220, 20, 24, 624, 3966, 7373, 1616, 311, 1744, 911, 419, 374, 311, 1430, 311, 990, 7525,
                     429, 646, 2990, 311, 75240, 476, 264, 4778, 1372, 2163, 220, 20, 24, 624, 2679, 582, 4774, 311, 990, 279, 7772, 5109, 1156, 323, 1221,
                     5602, 862, 19554, 448, 9155, 5109, 11, 582, 2578, 633, 12128, 311, 279, 2169, 13, 715, 82796, 220, 22, 17, 323, 220, 17, 18, 5310, 11, 582,
                     2578, 32256, 220, 17, 18, 504, 220, 22, 17, 311, 633, 220, 19, 24, 13, 1988, 582, 1184, 311, 7500, 311, 5545, 220, 20, 24, 13, 30370, 220,
                     16, 15, 311, 220, 19, 24, 1558, 279, 14068, 624, 4416, 11, 279, 23606, 1035, 1401, 2494, 1075, 320, 22, 17, 481, 220, 17, 18, 8, 488, 1599,
                     284, 220, 20, 24, 624, 50, 6383, 7766, 320, 22, 17, 481, 220, 17, 18, 8, 582, 614, 220, 19, 24, 11, 773, 320, 19, 24, 488, 1599, 8, 284,
                     220, 20, 24, 624, 4792, 3363, 1599, 284, 220, 20, 24, 481, 220, 19, 24, 11, 892, 374, 220, 16, 15, 624, 7039, 582, 1414, 582, 1184, 220,
                     16, 15, 11, 323, 582, 614, 279, 9664, 1372, 220, 22, 15, 13, 1205, 1184, 311, 990, 432, 311, 1855, 220, 16, 15, 624, 10061, 594, 1490,
                     1246, 1112, 1416, 582, 21749, 220, 22, 15, 553, 220, 22, 11, 582, 633, 220, 16, 15, 624, 4416, 279, 23606, 4278, 700, 311, 387, 25, 220,
                     22, 15, 608, 220, 22, 488, 220, 22, 17, 481, 220, 17, 18, 284, 220, 20, 24, 624, 522, 26865, 397, 27, 9217, 29, 220, 22, 15, 608, 220, 22,
                     488, 220, 22, 17, 481, 220, 17, 18, 690, 9217, 29, 151645],
                    [8704, 582, 525, 3330, 369, 458, 23606, 429, 3059, 304, 220, 20, 24, 11, 323, 582, 2299, 7199, 311, 1667, 1817, 1372, 508, 22, 15, 11, 220,
                     22, 17, 11, 220, 23, 15, 11, 220, 17, 18, 60, 1172, 3055, 11, 279, 5795, 374, 311, 36635, 1493, 5109, 1526, 6770, 34784, 7525, 13, 3776,
                     3204, 1616, 311, 5486, 419, 374, 311, 1191, 448, 1045, 30339, 28117, 323, 1490, 421, 582, 646, 17331, 518, 220, 20, 24, 13, 6771, 594,
                     2908, 279, 3881, 5109, 323, 1430, 34171, 1105, 304, 2155, 5510, 13, 10696, 279, 6672, 1948, 1045, 5109, 686, 7540, 2494, 3265, 311, 220,
                     20, 24, 13, 6771, 594, 1430, 220, 23, 15, 481, 220, 17, 18, 311, 633, 220, 20, 22, 11, 1221, 1490, 421, 62514, 220, 22, 15, 323, 220, 22,
                     17, 686, 5545, 220, 20, 24, 13, 690, 26865, 397, 1654, 614, 220, 23, 15, 481, 220, 17, 18, 284, 220, 20, 22, 13, 1205, 1184, 311, 835, 705,
                     448, 220, 20, 24, 13, 4695, 11, 582, 1184, 311, 7500, 220, 20, 22, 311, 633, 311, 220, 20, 24, 13, 3776, 1616, 311, 653, 419, 374, 553,
                     1667, 220, 22, 17, 481, 220, 22, 15, 284, 220, 17, 13, 5005, 7842, 419, 220, 17, 311, 220, 20, 22, 686, 2968, 220, 20, 24, 13, 715, 10061,
                     594, 88859, 419, 510, 27, 9217, 29, 320, 23, 15, 481, 220, 17, 18, 8, 488, 320, 22, 17, 481, 220, 22, 15, 8, 690, 9217, 29, 151645],
                    [1205, 614, 3040, 2661, 5109, 25, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 13, 5633, 5795, 374, 311, 990, 1817,
                     1372, 6896, 3055, 323, 3455, 6770, 34784, 7525, 311, 5545, 279, 1102, 315, 220, 20, 24, 13, 4710, 2679, 582, 1401, 518, 279, 2661, 5109,
                     11, 1156, 12831, 279, 23606, 5944, 11, 432, 4977, 17367, 429, 4285, 5256, 476, 75240, 1410, 2990, 601, 311, 220, 20, 24, 4152, 311, 279,
                     12929, 2058, 9664, 304, 1741, 7525, 448, 279, 5109, 2661, 13, 2055, 11, 582, 1184, 311, 1744, 315, 803, 6351, 7525, 1667, 46444, 323,
                     12804, 11, 1576, 807, 646, 1492, 7949, 279, 5109, 803, 29720, 382, 10061, 594, 2908, 279, 21937, 3019, 14319, 29208, 553, 7842, 323, 32256,
                     287, 825, 738, 315, 5109, 11, 1221, 1667, 12804, 311, 633, 438, 3265, 438, 3204, 311, 220, 20, 24, 13, 6771, 594, 1430, 510, 7, 22, 17,
                     488, 220, 23, 15, 8, 608, 220, 22, 15, 284, 220, 16, 20, 17, 608, 220, 22, 15, 892, 374, 10078, 803, 1091, 220, 17, 624, 5847, 11, 32256,
                     220, 17, 18, 510, 16, 20, 17, 608, 220, 22, 15, 481, 220, 17, 18, 284, 220, 17, 13, 16, 22, 16, 19, 481, 220, 17, 18, 892, 374, 2238, 2613,
                     624, 3838, 4977, 803, 18580, 1410, 387, 510, 22, 17, 488, 220, 17, 18, 481, 320, 23, 15, 608, 220, 22, 15, 8, 284, 220, 24, 20, 481, 220,
                     16, 13, 16, 19, 17, 24, 284, 220, 24, 18, 13, 23, 20, 22, 16, 892, 374, 2058, 537, 4396, 382, 10061, 594, 1430, 2441, 10601, 510, 22, 17,
                     488, 220, 22, 15, 481, 220, 23, 15, 481, 220, 17, 18, 284, 220, 21, 24, 481, 220, 17, 18, 284, 220, 19, 21, 13, 4695, 11, 582, 1184, 311,
                     7949, 432, 311, 220, 20, 24, 11, 582, 1184, 311, 990, 46444, 1790, 11, 8450, 582, 15282, 510, 22, 17, 353, 320, 23, 15, 608, 220, 17, 18,
                     8, 284, 220, 22, 17, 353, 220, 18, 13, 19, 22, 23, 18, 284, 220, 17, 19, 24, 13, 22, 23, 24, 21, 892, 374, 1602, 3265, 714, 537, 220, 20,
                     24, 26, 279, 9664, 5666, 1265, 387, 264, 41029, 79796, 75240, 476, 5256, 13, 690, 26865, 1339, 7039, 11, 1283, 12831, 11, 279, 23606, 1969,
                     387, 510, 27, 9217, 29, 220, 22, 17, 481, 220, 17, 18, 488, 220, 22, 15, 608, 220, 23, 15, 690, 9217, 397, 522, 9217, 1339, 10061, 594,
                     19633, 432, 1182, 369, 13295, 510, 27, 26865, 29, 220, 22, 17, 481, 220, 17, 18, 488, 220, 22, 15, 608, 220, 23, 15, 284, 220, 19, 24, 488,
                     220, 15, 13, 23, 22, 20, 284, 220, 20, 24, 13, 23, 22, 20, 13, 690, 26865, 1339, 49284, 264, 12128, 1401, 518, 419, 11, 432, 594, 537,
                     23638, 220, 20, 24, 11, 714, 2661, 279, 16982, 315, 1667, 678, 5109, 3055, 323, 2500, 7525, 11, 279, 18093, 374, 4658, 366, 9217, 29, 220,
                     22, 17, 481, 220, 17, 18, 488, 220, 22, 15, 608, 220, 23, 15, 690],
                    [358, 1184, 311, 1855, 458, 23606, 1667, 279, 5109, 220, 20, 21, 11, 220, 21, 23, 11, 220, 23, 20, 11, 323, 220, 16, 23, 429, 3059, 304,
                     220, 20, 22, 13, 358, 646, 28066, 1817, 1372, 1172, 3055, 13, 6771, 594, 1191, 553, 12831, 421, 625, 35268, 5109, 5961, 476, 17719, 1105,
                     1526, 34784, 7525, 686, 2990, 311, 279, 1290, 1102, 624, 2679, 358, 21749, 220, 16, 23, 553, 220, 18, 11, 429, 3059, 304, 220, 21, 13,
                     10083, 1283, 429, 11, 358, 1410, 13581, 32256, 476, 912, 1045, 5109, 311, 633, 12128, 311, 847, 2169, 315, 220, 20, 22, 13, 358, 1083,
                     2908, 5256, 1948, 1045, 315, 279, 8131, 5109, 3918, 26865, 397, 28715, 389, 16585, 17879, 11, 279, 23606, 429, 5711, 1817, 315, 279, 5109,
                     6896, 3055, 323, 16819, 220, 20, 22, 1265, 387, 510, 27, 9217, 29, 220, 23, 20, 481, 220, 21, 23, 488, 220, 20, 21, 608, 220, 16, 23, 690,
                     9217, 397, 522, 26865, 397, 10061, 752, 1438, 432, 1495, 311, 10146, 510, 12, 220, 20, 21, 608, 220, 16, 23, 284, 220, 18, 13, 16, 16, 16,
                     9338, 12, 220, 21, 23, 481, 220, 18, 13, 16, 16, 16, 1112, 284, 220, 21, 19, 13, 23, 23, 23, 9338, 12, 220, 23, 20, 481, 220, 21, 19, 13,
                     23, 23, 23, 1112, 284, 220, 17, 15, 13, 16, 16, 16, 9338, 12, 220, 17, 15, 13, 16, 16, 16, 1112, 488, 220, 20, 21, 608, 220, 16, 23, 284,
                     220, 20, 22, 198, 2132, 4977, 279, 5666, 5181, 3556, 374, 10078, 15114, 4152, 311, 51562, 13, 6771, 594, 653, 264, 3974, 1779, 510, 12,
                     220, 20, 21, 608, 220, 16, 23, 284, 220, 18, 13, 16, 16, 16, 1112, 320, 46385, 12122, 12804, 340, 12, 220, 21, 23, 481, 220, 18, 13, 16,
                     16, 16, 1112, 284, 220, 21, 19, 13, 23, 23, 23, 9338, 12, 220, 23, 20, 481, 220, 21, 19, 13, 23, 23, 23, 1112, 284, 220, 17, 15, 13, 16,
                     16, 16, 9338, 12, 220, 17, 15, 13, 16, 16, 16, 1112, 488, 220, 18, 13, 16, 16, 16, 1112, 284, 220, 20, 18, 13, 17, 17, 17, 9338, 1986,
                     2058, 3171, 944, 5545, 220, 20, 22, 13, 6771, 594, 7500, 279, 1616, 582, 990, 279, 5109, 13, 1032, 2682, 5853, 279, 4522, 315, 5256, 2578,
                     387, 2664, 510, 27, 9217, 29, 220, 21, 23, 488, 320, 23, 20, 481, 220, 20, 21, 481, 220, 16, 23, 608, 220, 17, 8, 690, 9217, 397, 522,
                     26865, 397, 522, 26865, 397, 10061, 752, 7683, 279, 31728, 23606, 510, 12, 220, 16, 23, 608, 220, 17, 284, 220, 24, 198, 12, 220, 23, 20,
                     481, 220, 20, 21, 481, 220, 24, 284, 220, 17, 15, 198, 12, 220, 21, 23, 488, 220, 17, 15, 284, 220, 23, 23, 271, 785, 23606, 220, 21, 23,
                     488, 320, 23, 20, 481, 220, 20, 21, 481, 220, 16, 23, 608, 220, 17, 8, 12440, 5711, 678, 279, 5109, 6896, 3055, 323, 16819, 220, 23, 23,
                     624, 12549, 279, 4024, 2169, 315, 220, 20, 22, 4157],
                    [5338, 398, 11, 220, 20, 22, 374, 1602, 3265, 311, 220, 20, 21, 323, 220, 21, 23, 892, 525, 2176, 2661, 5109, 13, 3776, 1616, 311, 633, 311,
                     220, 20, 22, 374, 553, 7842, 476, 32256, 287, 264, 1372, 553, 220, 16, 13, 57633, 429, 678, 5109, 646, 1172, 387, 1483, 3055, 11, 220, 16,
                     23, 646, 387, 279, 1372, 553, 892, 311, 32256, 220, 20, 21, 311, 633, 220, 20, 22, 13, 1988, 279, 5109, 525, 220, 20, 21, 11, 220, 21, 23,
                     11, 220, 23, 20, 11, 323, 220, 16, 23, 11, 6857, 315, 892, 525, 220, 16, 11, 323, 32256, 287, 220, 16, 23, 504, 220, 20, 21, 2765, 944,
                     2990, 601, 311, 220, 21, 23, 476, 220, 23, 20, 13, 2055, 11, 429, 3171, 944, 975, 3918, 26865, 397, 32, 2155, 5486, 2578, 13186, 49702,
                     7525, 2474, 49702, 646, 1492, 8172, 279, 23606, 1667, 279, 5080, 5109, 320, 21, 23, 323, 220, 23, 20, 568, 18680, 1881, 69715, 17779, 553,
                     220, 16, 13, 20, 646, 13581, 2968, 601, 220, 19, 20, 13, 18, 18, 1112, 476, 220, 20, 22, 448, 51562, 476, 44868, 3363, 13, 1988, 220, 16,
                     13, 20, 4436, 944, 458, 7546, 13, 4354, 11, 432, 6081, 20017, 429, 12804, 5310, 448, 220, 16, 23, 438, 264, 8168, 1231, 387, 3204, 624,
                     37175, 279, 5109, 220, 21, 23, 11, 220, 16, 23, 11, 323, 220, 23, 20, 13, 1416, 220, 21, 23, 17779, 553, 220, 16, 13, 20, 16819, 220, 19,
                     20, 323, 582, 32256, 220, 16, 23, 504, 432, 11, 582, 2578, 5486, 220, 20, 22, 13, 4354, 11, 220, 16, 23, 17779, 553, 220, 16, 13, 20,
                     16819, 220, 16, 17, 11, 773, 220, 21, 23, 481, 220, 16, 17, 284, 220, 20, 21, 11, 323, 220, 20, 21, 488, 220, 16, 284, 220, 20, 22, 624,
                     1986, 6696, 601, 2326, 5109, 311, 975, 448, 25, 220, 21, 23, 11, 220, 16, 23, 11, 323, 220, 16, 13, 1597, 279, 11737, 374, 2115, 438, 582,
                     738, 15102, 13, 1752, 419, 23606, 11, 1077, 594, 312, 6763, 1667, 6770, 34784, 7525, 624, 522, 26865, 397, 27, 9217, 29, 320, 21, 23, 481,
                     220, 16, 23, 488, 220, 16, 8, 608, 220, 16, 690, 9217, 397, 1986, 23606, 46918, 311, 25, 1781, 21, 23, 481, 220, 16, 23, 8, 488, 220, 16,
                     8, 608, 220, 16, 11, 892, 15491, 9606, 311, 220, 20, 21, 488, 220, 16, 11, 892, 16819, 220, 20, 22, 13, 8704, 678, 7525, 1265, 387, 10660,
                     304, 279, 1973, 807, 4994, 11, 419, 6696, 601, 279, 1590, 4226, 25, 320, 20, 22, 608, 220, 16, 8, 284, 220, 20, 22, 13, 151645],
                    [5338, 398, 11, 220, 20, 22, 646, 387, 13302, 438, 220, 20, 15, 488, 220, 22, 11, 773, 825, 315, 279, 27459, 1035, 21058, 419, 13, 3776,
                     4285, 1616, 374, 311, 3158, 220, 20, 15, 438, 264, 10601, 315, 279, 5109, 220, 20, 21, 11, 220, 21, 23, 11, 323, 220, 16, 23, 11, 323,
                     1221, 15963, 432, 448, 220, 22, 1667, 279, 7525, 2500, 13, 4695, 11, 220, 20, 21, 481, 220, 16, 23, 284, 220, 18, 23, 323, 220, 21, 23,
                     481, 220, 16, 23, 284, 220, 20, 15, 11, 773, 582, 646, 15963, 1493, 311, 1281, 220, 18, 23, 488, 220, 20, 15, 13, 1205, 1431, 1184, 220,
                     22, 11, 892, 1410, 614, 1012, 279, 4843, 1372, 2115, 916, 438, 264, 4361, 476, 438, 949, 315, 2441, 1372, 13, 6771, 594, 1430, 311, 4946,
                     220, 20, 21, 438, 220, 18, 23, 488, 220, 16, 23, 323, 1221, 912, 220, 22, 11, 438, 220, 18, 23, 488, 220, 16, 23, 488, 220, 22, 284, 220,
                     21, 18, 11, 892, 15491, 9606, 311, 220, 20, 15, 488, 220, 22, 979, 220, 16, 23, 374, 32256, 291, 3918, 26865, 397, 27, 9217, 2235, 20, 21,
                     481, 220, 16, 23, 8, 488, 320, 21, 23, 481, 220, 16, 23, 481, 220, 22, 12533, 9217, 29, 151645],
                    [358, 1184, 311, 1352, 458, 23606, 1667, 279, 5109, 220, 20, 21, 11, 220, 21, 23, 11, 220, 23, 20, 11, 323, 220, 16, 23, 11, 448, 678, 7525,
                     1660, 6770, 34784, 11, 323, 1817, 15723, 1483, 6896, 3055, 13, 576, 2169, 1372, 374, 220, 20, 22, 13, 690, 26865, 397, 82796, 279, 2169,
                     1372, 220, 20, 22, 11, 432, 4977, 3265, 311, 279, 1372, 220, 20, 21, 13, 358, 646, 32256, 220, 16, 504, 220, 20, 21, 11, 892, 1035, 2968,
                     752, 220, 20, 22, 13, 715, 16429, 279, 1372, 220, 16, 23, 11, 358, 646, 32256, 220, 16, 23, 504, 220, 20, 21, 11, 714, 429, 1035, 1102,
                     304, 220, 18, 23, 11, 537, 220, 20, 22, 13, 12090, 11, 358, 3278, 1490, 421, 358, 646, 990, 12804, 476, 1008, 14609, 7455, 13, 690, 26865,
                     397, 40, 13083, 358, 646, 21749, 220, 20, 21, 553, 220, 24, 320, 8206, 5711, 220, 20, 21, 323, 10901, 752, 448, 220, 24, 389, 279, 1008,
                     3108, 701, 323, 421, 358, 32256, 476, 912, 220, 24, 34901, 11, 358, 646, 633, 3265, 311, 220, 20, 22, 13, 33763, 11, 49702, 553, 220, 24,
                     1231, 7540, 264, 12122, 11, 892, 4436, 944, 10507, 13, 93210, 287, 476, 7842, 220, 16, 23, 504, 220, 20, 21, 476, 220, 23, 20, 2578, 537,
                     975, 2661, 279, 3561, 358, 2776, 3330, 369, 624, 10061, 594, 1430, 2441, 5486, 13, 1416, 358, 2908, 279, 23606, 304, 264, 803, 11521, 1616,
                     11, 358, 2578, 1744, 911, 7842, 476, 32256, 287, 9155, 5109, 311, 220, 20, 21, 13, 8704, 220, 16, 23, 1410, 387, 458, 14704, 11, 358, 2578,
                     1184, 311, 4347, 432, 16925, 624, 40, 3278, 1273, 279, 23606, 25, 320, 21, 23, 481, 220, 23, 20, 8, 608, 220, 16, 23, 488, 220, 20, 21,
                     624, 522, 26865, 397, 7039, 11, 1077, 752, 11047, 419, 23606, 624, 27, 9217, 29, 320, 21, 23, 481, 220, 23, 20, 8, 608, 220, 16, 23, 488,
                     220, 20, 21, 690, 9217, 29, 284, 481, 16, 22, 608, 220, 16, 23, 488, 220, 20, 21, 624, 10061, 594, 15442, 419, 25, 481, 16, 22, 608, 220,
                     16, 23, 284, 481, 15, 13, 24, 19, 19, 19, 9338, 12, 15, 13, 24, 19, 19, 19, 1112, 488, 220, 20, 21, 284, 220, 20, 20, 13, 15, 20, 20, 21,
                     9338, 785, 1102, 374, 537, 6896, 220, 20, 22, 11, 892, 13230, 358, 1184, 311, 312, 5655, 19642, 279, 5109, 323, 7525, 624, 6025, 4623,
                     17879, 11, 358, 13083, 358, 1184, 311, 15516, 2692, 369, 678, 3204, 7525, 323, 27459, 13, 6771, 594, 1430, 2441, 5486, 624, 24365, 766, 8,
                     1032, 5655, 25510, 1095, 11, 358, 13083, 429, 421, 358, 990, 279, 1372, 220, 21, 23, 311, 1492, 5545, 1039, 2169, 11, 358, 646, 1401, 369,
                     264, 6169, 1616, 311, 990, 220, 20, 21, 11, 220, 23, 20, 11, 323, 220, 16, 23, 311, 4347, 323, 5545, 220, 20, 22, 13, 690, 26865, 397, 32,
                     3204, 6514, 1410, 387, 1667, 5256, 476, 46444, 92296, 311, 3331, 279, 1590, 2629, 382, 4416, 11, 1077, 752, 1273],
                    [5338, 398, 11, 358, 5293, 429, 220, 20, 22, 374, 3265, 311, 279, 2629, 315, 220, 21, 23, 323, 220, 16, 23, 11, 892, 6696, 220, 23, 21, 13,
                     2938, 594, 3403, 220, 20, 22, 13, 93210, 287, 220, 17, 24, 504, 220, 23, 21, 1035, 633, 601, 3265, 311, 220, 20, 22, 11, 323, 220, 17, 24,
                     8573, 311, 387, 279, 2629, 315, 220, 20, 21, 481, 220, 17, 23, 284, 220, 20, 21, 481, 220, 23, 20, 488, 220, 16, 23, 13, 15277, 11, 358,
                     646, 990, 1493, 5109, 311, 1352, 458, 23606, 13, 1205, 646, 1191, 448, 220, 21, 23, 481, 320, 20, 21, 481, 220, 23, 20, 488, 220, 16, 23,
                     8, 323, 32256, 220, 17, 24, 3918, 26865, 397, 27, 9217, 29, 220, 21, 23, 481, 320, 20, 21, 481, 220, 23, 20, 488, 220, 16, 23, 8, 481, 220,
                     17, 24, 690, 9217, 29, 151645],
                    [5338, 11, 358, 686, 1490, 421, 358, 646, 990, 279, 5109, 5961, 311, 633, 3265, 311, 220, 20, 22, 13, 506, 723, 91355, 448, 1493, 37906, 11,
                     1741, 264, 4285, 8282, 4278, 13, 358, 3278, 1430, 311, 5545, 264, 1372, 3265, 311, 220, 20, 22, 553, 34171, 1378, 315, 279, 5109, 13, 576,
                     5109, 220, 20, 21, 323, 220, 16, 23, 912, 705, 311, 220, 22, 19, 11, 892, 374, 2238, 1550, 13, 220, 21, 23, 323, 220, 23, 20, 2629, 311,
                     220, 16, 20, 18, 11, 892, 374, 1083, 2238, 1550, 13, 690, 26865, 1339, 5847, 11, 358, 5293, 429, 220, 21, 23, 481, 220, 16, 23, 284, 220,
                     20, 15, 11, 892, 374, 3265, 311, 220, 20, 22, 13, 5005, 11, 358, 3278, 990, 12804, 323, 75240, 311, 1281, 264, 6915, 27075, 13, 715, 27,
                     9217, 2235, 21, 23, 481, 220, 16, 23, 8, 608, 220, 20, 21, 488, 220, 23, 20, 481, 220, 21, 23, 284, 220, 20, 22, 522, 9217, 29, 4710,
                     11209, 11, 389, 21937, 11, 419, 3059, 304, 510, 27, 9217, 29, 20, 15, 608, 220, 20, 21, 488, 220, 23, 20, 481, 220, 21, 23, 284, 220, 19,
                     13, 17, 23, 20, 22, 488, 220, 23, 20, 481, 220, 21, 23, 21103, 230, 220, 17, 16, 13, 17, 23, 20, 22, 366, 9217, 1339, 1986, 3171, 944,
                     1102, 304, 220, 20, 22, 11, 773, 358, 1184, 311, 75655, 847, 5486, 13, 6771, 594, 1430, 220, 23, 20, 481, 220, 21, 23, 284, 220, 16, 22,
                     13, 5005, 11, 358, 646, 912, 220, 16, 23, 323, 32256, 220, 20, 21, 311, 633, 3265, 311, 220, 20, 22, 624, 27, 9217, 2235, 23, 20, 481, 220,
                     21, 23, 8, 488, 220, 16, 23, 481, 220, 20, 21, 284, 220, 20, 22, 522, 9217, 1339, 7039, 11, 1077, 594, 10146, 419, 23606, 624, 522, 26865,
                     397, 27, 9217, 2235, 23, 20, 481, 220, 21, 23, 8, 488, 220, 16, 23, 481, 220, 20, 21, 284, 220, 20, 22, 522, 9217, 29, 151645],
                    [5338, 398, 11, 279, 2169, 1372, 374, 220, 20, 22, 13, 21131, 518, 279, 1140, 11, 279, 1372, 220, 20, 21, 13352, 700, 438, 220, 20, 22, 481,
                     220, 16, 504, 1039, 1140, 13, 6771, 594, 1779, 421, 220, 20, 21, 323, 220, 16, 646, 387, 14257, 504, 279, 3800, 1667, 279, 2500, 7525,
                     17973, 11, 85922, 11777, 608, 66233, 26865, 397, 1654, 646, 3158, 220, 20, 22, 481, 220, 20, 21, 438, 220, 16, 11, 714, 279, 8645, 374,
                     311, 6923, 220, 16, 1667, 279, 9664, 5109, 323, 19624, 624, 82796, 279, 1372, 220, 16, 23, 11, 49702, 432, 553, 220, 21, 23, 1410, 2968,
                     601, 264, 11924, 897, 11, 323, 32256, 287, 264, 13348, 315, 429, 504, 220, 21, 23, 476, 220, 23, 20, 1410, 1492, 304, 31045, 220, 20, 22,
                     624, 38606, 279, 12804, 315, 220, 16, 23, 553, 220, 21, 23, 11, 582, 633, 220, 16, 23, 14, 21, 23, 284, 220, 15, 13, 17, 21, 19, 22, 979,
                     9848, 7145, 11, 892, 4436, 944, 23560, 369, 1039, 2169, 315, 220, 16, 13, 4354, 11, 582, 4363, 646, 5452, 419, 311, 633, 1039, 12685, 897,
                     553, 62514, 279, 7525, 323, 279, 5109, 3897, 3055, 624, 522, 26865, 397, 7039, 279, 4522, 374, 2797, 510, 27, 9217, 29, 320, 23, 20, 481,
                     220, 21, 23, 8, 608, 220, 16, 23, 353, 220, 16, 488, 220, 20, 21, 690, 9217, 29, 892, 15491, 9606, 311, 366, 9217, 29, 220, 16, 22, 14, 16,
                     23, 353, 220, 16, 488, 220, 20, 21, 690, 9217, 397, 1249, 5545, 220, 20, 22, 510, 27, 9217, 29, 284, 320, 16, 22, 14, 16, 23, 8, 353, 220,
                     16, 23, 488, 220, 20, 21, 284, 220, 16, 22, 488, 220, 20, 21, 284, 220, 20, 22, 690, 9217, 1339, 44500, 11, 279, 7493, 12440, 5711, 279,
                     5109, 508, 20, 21, 11, 220, 21, 23, 11, 220, 23, 20, 11, 220, 16, 23, 60, 323, 279, 7525, 311, 6144, 220, 20, 22, 13, 151645],
                    [358, 1184, 311, 990, 279, 5109, 220, 20, 21, 11, 220, 21, 23, 11, 220, 23, 20, 11, 323, 220, 16, 23, 6896, 3055, 311, 633, 264, 1102, 315,
                     220, 20, 22, 13, 358, 1265, 5185, 429, 12804, 646, 975, 448, 25780, 311, 7540, 4361, 5109, 11, 714, 358, 3278, 1083, 2908, 1008, 7525,
                     3918, 26865, 397, 82796, 7546, 12804, 323, 6770, 7525, 1075, 5256, 11, 75240, 11, 46444, 11, 323, 12804, 448, 4361, 5109, 13, 6771, 752,
                     1779, 2155, 27459, 510, 27, 9217, 29, 320, 23, 20, 488, 220, 16, 23, 481, 220, 21, 23, 8, 608, 220, 20, 21, 690, 9217, 397, 40, 3278,
                     10146, 419, 510, 16, 13, 5145, 448, 279, 7493, 25, 320, 23, 20, 488, 220, 16, 23, 481, 220, 21, 23, 8, 608, 220, 20, 21, 198, 17, 13,
                     20517, 279, 2629, 25, 220, 23, 20, 488, 220, 16, 23, 284, 220, 16, 15, 18, 198, 18, 13, 93210, 220, 21, 23, 504, 220, 16, 15, 18, 25, 220,
                     16, 15, 18, 481, 220, 21, 23, 284, 220, 18, 20, 198, 19, 13, 17375, 11, 21749, 553, 220, 20, 21, 25, 220, 18, 20, 608, 220, 20, 21, 284,
                     220, 15, 13, 21, 17, 20, 198, 1986, 3171, 944, 5008, 975, 13, 6771, 594, 1430, 2441, 10601, 1447, 27, 9217, 29, 320, 23, 20, 481, 220, 20,
                     21, 8, 488, 320, 16, 23, 608, 220, 21, 23, 8, 690, 9217, 397, 40, 3278, 10146, 510, 16, 13, 5145, 448, 279, 7493, 25, 320, 23, 20, 481,
                     220, 20, 21, 8, 488, 320, 16, 23, 608, 220, 21, 23, 340, 17, 13, 55080, 1948, 220, 23, 20, 323, 220, 20, 21, 25, 220, 23, 20, 481, 220, 20,
                     21, 284, 220, 17, 24, 198, 18, 13, 14489, 220, 16, 23, 608, 220, 21, 23, 374, 13187, 220, 15, 13, 17, 21, 19, 22, 320, 970, 264, 29952,
                     340, 19, 13, 8116, 315, 220, 17, 24, 323, 220, 15, 13, 17, 21, 19, 22, 374, 13187, 220, 17, 24, 13, 17, 21, 19, 22, 198, 1986, 4436, 944,
                     220, 20, 22, 2987, 11, 714, 432, 594, 3265, 3322, 304, 10740, 3793, 13, 8704, 358, 1184, 458, 4734, 6291, 11, 1077, 594, 1430, 2441, 10601,
                     1447, 27, 9217, 29, 320, 23, 20, 481, 220, 21, 23, 8, 488, 220, 20, 21, 608, 220, 16, 23, 690, 9217, 397, 40, 3278, 10146, 510, 16, 13,
                     5145, 448, 279, 7493, 25, 320, 23, 20, 481, 220, 21, 23, 8, 488, 220, 20, 21, 608, 220, 16, 23, 198, 17, 13, 55080, 220, 23, 20, 481, 220,
                     21, 23, 284, 220, 16, 22, 198, 18, 13, 14489, 220, 20, 21, 608, 220, 16, 23, 374, 13187, 220, 18, 13, 16, 16, 16, 16, 198, 19, 13, 30370,
                     220, 16, 22, 323, 220, 18, 13, 16, 16, 16, 16, 284, 220, 17, 15, 13, 16, 16, 16, 16, 198, 23322, 537, 6144, 311, 220, 20, 22, 13, 6771,
                     594, 1430, 825, 803, 10601, 1447, 27, 9217, 29, 320, 20, 21, 353, 220, 23, 20, 481, 220, 21, 23, 481, 220, 16, 23, 8]],
 'reasoning_steps': [['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'], ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'],
                     ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'], ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'],
                     ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'], ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'],
                     ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'], ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'],
                     ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'], ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'],
                     ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'], ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'],
                     ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'], ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'],
                     ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57'], ['68', '68 + 18 = 86', '86 + 56 = 142', '142 - 85 = 57', '57']]
}
# %%
reward_inputs.keys()
# %%
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import ModelConfig
from pprint import pp
import torch
import sys
sys.path.insert(0, '../methods/RL/utils')
from CoT_rewards import split_thoughts, compute_CoT_rewards

# %%
model_config = ModelConfig(model_name_or_path='Qwen/Qwen2.5-3B-Instruct',
        model_revision='main',
        torch_dtype='bfloat16',
        trust_remote_code=False,
        attn_implementation='flash_attention_2',
        use_peft=False,
        lora_r=32,
        lora_alpha=64,
        lora_dropout=0.1,
        lora_target_modules=['q_proj', 'v_proj'],
        lora_modules_to_save=None,
        lora_task_type='CAUSAL_LM',
        use_rslora=False,
        use_dora=False,
        load_in_8bit=False,
        load_in_4bit=False,
        bnb_4bit_quant_type='nf4',
        use_bnb_nested_quant=False)
model_path = model_config.model_name_or_path

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=model_config.trust_remote_code
)


model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=model_config.torch_dtype,
    trust_remote_code=model_config.trust_remote_code,
    attn_implementation=model_config.attn_implementation
)
print(f'# params: {sum(p.numel() for p in model.parameters()):,}')



# %%

for i, ids in enumerate(reward_inputs['completion_ids']):
    print("=" * 40 + f" {i} " + "=" * 40)
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
inds = [3, 6]
from pprint import pp
pp({k: [v[i] for i in inds] for k, v in reward_inputs.items()}, compact=True, width=160)
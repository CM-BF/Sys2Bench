import random
import re


def sc_output_extractor(algo_output):
    from collections import Counter
    answers = []
    for x in algo_output:
        answers.append(extract_plan(x))
            
    # answers = [x for x in algo_output if x is not None]
    counter = Counter(answers)
    if counter == {}:
        return None
    return counter.most_common(1)[0][0]


def extract_plan(text):
    pattern = r"<plan>(.*?)</plan>"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        print("No match found in output:", text)
        return ""

def generate_icl(examples, provide_think_icl=False, num_icl = 2, idx=None):
    
    if idx is not None:
        filtered_examples = [ex for i, ex in enumerate(examples) if i != idx]
    else:
        filtered_examples = sampled_examples
    
    sampled_examples = random.sample(filtered_examples, num_icl)
    if num_icl == 1:
        icl_text = "Here is an example problem:\n\n"
    else:
        icl_text = "Here are some example problems:\n\n"
    for example in sampled_examples:
        icl_text += f"Here is the initial state of the blocks: {example['init']}\n\nHere is the goal state of the blocks: {example['goal']}.\nShow your work in the <think> </think> tags. Return the final sequence of actions as the plan in the <plan> </plan> tags.\n"
        if provide_think_icl:
            icl_text += example['trace']
        else:
            icl_text += f"<think>To solve this problem, I need to come up with the right set of actions to achieve the goal.</think>\n<plan>\n{extract_plan(example['trace'])}\n</plan>\n\n"
    return icl_text

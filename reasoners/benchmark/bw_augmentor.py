import random
import re

def ordinal(n):
    """
    Convert an integer n to its ordinal representation as a string.
    For example, 1 -> '1st', 2 -> '2nd', 3 -> '3rd', 4 -> '4th', etc.
    """
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def generate_mapping(original_names, candidate_list):
    """
    Generate a one-to-one mapping from original_names to a randomly selected set
    of candidate_list values, ensuring no duplicate assignments.
    
    For candidate lists identical to original_names (used for a shuffled mapping),
    this function will re-shuffle until the resulting mapping differs from the original order.
    """
    if candidate_list == original_names:
        if len(original_names) == 1:
            mapping = original_names.copy()
        else:
            mapping = original_names.copy()
            while mapping == original_names:
                random.shuffle(mapping)
    else:
        mapping = random.sample(candidate_list, len(original_names))
    return dict(zip(original_names, mapping))

def apply_mapping(text, mapping):
    """
    Replace all occurrences of any original name with its mapped value in one pass.
    
    A single regular-expression pattern is compiled that matches any of the original names,
    and a callback function is used to replace each match with its mapped value.
    This avoids cyclic dependency issues that can occur with sequential replacements.
    """
    pattern = r'\b(' + '|'.join(map(re.escape, mapping.keys())) + r')\b'
    return re.sub(pattern, lambda match: mapping[match.group(0).lower()], text, flags=re.IGNORECASE)

def adjust_number_format(text):
    """
    Adjust text for number mappings so that occurrences like '1 block' become 'block 1'.
    """
    return re.sub(r'\b(\d+)\s+block\b', r'block \1', text)

def extract_original_names(text):
    """
    Extract unique block names from the given text.
    
    Searches for words immediately preceding 'block' (case-insensitive) and returns
    them in order of appearance.
    """
    pattern = r'\b(\w+)\s+block\b'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    seen = []
    for name in matches:
        if name.lower() not in [s.lower() for s in seen]:
            seen.append(name.lower())
    return seen

def generate_augmentations(init_text, goal_text, plan_text, num_augmentations=3, max_attempts=100):
    """
    Given init, goal, and plan texts, automatically extract the block names,
    then generate multiple augmentations using different candidate domains.
    
    Each augmentation mapping is ensured to be unique within its candidate type.
    Returns a dictionary with augmentation types as keys and lists of augmentations.
    Each augmentation includes transformed init, goal, and plan texts.
    """
    # Combine texts for extracting all block names.
    combined_text = init_text + " " + goal_text + " " + plan_text
    original_names = extract_original_names(combined_text)
    print(len(original_names))
    # Define candidate lists for various augmentation types.
    aug_candidates = {
        "colors": ["magenta", "cyan", "violet", "turquoise", "indigo", "gold",
                   "silver", "emerald", "ruby", "sapphire"],
        "numbers": [f"{ordinal(i)}" for i in range(1, len(original_names) + 1)],
        "greek": ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", 
                  "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", 
                  "tau", "upsilon", "phi", "chi", "psi", "omega"],
        "alphabets": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "shuffled": original_names.copy()
    }
    
    augmentations = {}
    
    for aug_type, candidate_list in aug_candidates.items():
        augmentations[aug_type] = []
        seen_mappings = set()
        for _ in range(num_augmentations):
            attempts = 0
            while attempts < max_attempts:
                mapping = generate_mapping(original_names, candidate_list)
                # Use the order of original_names to create a tuple key.
                mapping_tuple = tuple(mapping[name] for name in original_names)
                if mapping_tuple not in seen_mappings:
                    seen_mappings.add(mapping_tuple)
                    break
                attempts += 1
            if attempts == max_attempts:
                print(f"Warning: Could not generate a unique mapping for {aug_type} after {max_attempts} attempts.")
                continue
            aug_init = apply_mapping(init_text, mapping)
            aug_goal = apply_mapping(goal_text, mapping)
            aug_plan = apply_mapping(plan_text, mapping)
                
            augmentation_data = {
                "mapping": mapping,
                "init": aug_init,
                "goal": aug_goal,
                "plan": aug_plan
            }
            augmentations[aug_type].append(augmentation_data)
    
    return augmentations

# ---------------------------
# Example usage:
init_example = '''the red block is clear, the orange block is clear, the hand is empty, the red block is on top of the yellow block, the yellow block is on top of the blue block, the blue block is on the table and the orange block is on the table the red block is on top of the orange block'''

goal_example = '''the blue block is clear, the orange block is clear, the hand is empty, the blue block is on top of the red block, the red block is on the table and the orange block is on the table the orange block is on top of the blue block'''
plan_example = '''pick up the orange block
stack the orange block on top of the blue block
[PLAN END]'''

# augmented_data = generate_augmentations(init_example, goal_example, plan_example, num_augmentations=3)

# for aug_type, aug_list in augmented_data.items():
#     print(f"Augmentation Type: {aug_type}")
#     for idx, data in enumerate(aug_list, 1):
#         print(f"Augmentation {idx}:")
#         print("Mapping:", data["mapping"])
#         print("Transformed Init:", data["init"])
#         print("Transformed Goal:", data["goal"])
#         print("Transformed Plan:", data["plan"])
#         print("-" * 40)
#     print("=" * 80)

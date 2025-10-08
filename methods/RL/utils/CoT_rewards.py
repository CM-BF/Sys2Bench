from typing import Union, Any
import re
from pprint import pp
from tqdm import tqdm 
import textwrap

import torch
from torch.nn.utils.rnn import pad_sequence
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast
from transformers import BatchEncoding
from trl.trainer.utils import selective_log_softmax

PROMPT_IDS = 'prompt_inputs'
PROMPT_MASK = 'prompt_attention_mask'
THOUGHT_IDS = 'thought_ids'
ANSWER_IDS = 'answer_ids'

def wrap_text(text: str):
    return textwrap.fill(text, width=80)

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
        print()
        print(wrap_text(completion))
        print()
        for thought in thoughts:
            print(f">>> {wrap_text(thought)}")
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
    for thought_idx in tqdm(range(max_num_thoughts + 1), disable=not verbose):
 
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
            answer_prob = avg_answer_ps[batch_idx, 0]
            print(f"Prob: {answer_prob:.4f}")
            answer_tokens = [tokenizer.decode(id_) for id_ in curr_answer_ids]
            answer_token_probs = per_token_answer_ps_list[0][batch_idx]
            print(wrap_text(", ".join([f"'{t}': {p:.4f}" for p, t in zip(answer_token_probs, answer_tokens)])))
            print()      
        for i, end_idx in enumerate(end_indices):
            reward_tensor[batch_idx, end_idx] = delta_prob[i]
            answer_prob = avg_answer_ps[batch_idx, i + 1]
            if verbose:
                start_idx = 0 if i == 0 else end_indices[i - 1] + 1
                curr_thought_tokens = curr_thought_ids[start_idx:end_idx + 1]
                curr_thought_text = tokenizer.decode(curr_thought_tokens, skip_special_tokens=True).strip()
                print()
                print(f'Thought: "{wrap_text(curr_thought_text)}"')
                print(f'Reward: {reward_tensor[batch_idx, end_idx]:.4f}, Prob: {answer_prob:.4f}')
    return reward_tensor


if __name__ == "__main__":

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
             '<think>'] * 3,
        'completions': [' I need to manipulate the numbers 70, 72, 80, and 23 using basic arithmetic operations so that the result is 59. \n'
                        'The key numbers are 80 and 23, as they are quite far from 59. A subtraction from 80 could help. If I subtract 23 from 80, I get 57. From '
                        "there, I'll need to adjust it to 59, which means an addition of 2. \n"
                        'So, 80 - 23 equals 57. To get to 59, I need 2. The numbers 23 and 72 have 23, so I can use 72 - 23 = 49 and then add 2 to 49 to get 59. \n'
                        'That means I can use these operations on 72, 23, and the final subtraction from 80 to get to 59.\n'
                        '</think>\n'
                        '<answer> (72 - 23) + (80 - 70) </answer>',
                        * [" Since we are looking for an equation that results in 59, and we're limited to using each number [70, 72, 80, 23] only once, the goal is to "
                        'manipulate these numbers through basic arithmetic operations. One possible way to approach this is to start with some straightforward '
                        "calculations and see if we can arrive at 59. Let's consider the known numbers and try combining them in different ways. Maybe the difference "
                        "between some numbers will yield something close to 59. Let's try 80 - 23 to get 57, then see if manipulating 70 and 72 will reach 59. "
                        '</think>\n'
                        'We have 80 - 23 = 57. We need to end up with 59. Now, we need to adjust 57 to get to 59. One way to do this is by using 72 - 70 = 2. Then '
                        'adding this 2 to 57 will give 59. \n'
                        "Let's formulate this:\n"
                        '<answer> (80 - 23) + (72 - 70) </answer>'] * 2],
        'expression': ['(72 - 23) + (80 - 70)', '(72 - 23) + (80 - 70)', '(80 - 23) + (72 - 70)'],
        'completion_ids': [[358, 1184, 311, 36635, 279, 5109, 220, 22, 15, 11, 220, 22, 17, 11, 220, 23, 15, 11, 323, 220, 17, 18, 1667, 6770, 34784, 7525, 773, 429,
                            279, 1102, 374, 220, 20, 24, 13, 715, 785, 1376, 5109, 525, 220, 23, 15, 323, 220, 17, 18, 11, 438, 807, 525, 5008, 3041, 504, 220, 20, 24,
                            13, 362, 75240, 504, 220, 23, 15, 1410, 1492, 13, 1416, 358, 32256, 220, 17, 18, 504, 220, 23, 15, 11, 358, 633, 220, 20, 22, 13, 5542,
                            1052, 11, 358, 3278, 1184, 311, 7500, 432, 311, 220, 20, 24, 11, 892, 3363, 458, 5256, 315, 220, 17, 13, 715, 4416, 11, 220, 23, 15, 481,
                            220, 17, 18, 16819, 220, 20, 22, 13, 2014, 633, 311, 220, 20, 24, 11, 358, 1184, 220, 17, 13, 576, 5109, 220, 17, 18, 323, 220, 22, 17,
                            614, 220, 17, 18, 11, 773, 358, 646, 990, 220, 22, 17, 481, 220, 17, 18, 284, 220, 19, 24, 323, 1221, 912, 220, 17, 311, 220, 19, 24, 311,
                            633, 220, 20, 24, 13, 715, 4792, 3363, 358, 646, 990, 1493, 7525, 389, 220, 22, 17, 11, 220, 17, 18, 11, 323, 279, 1590, 75240, 504, 220,
                            23, 15, 311, 633, 311, 220, 20, 24, 624, 522, 26865, 397, 27, 9217, 29, 320, 22, 17, 481, 220, 17, 18, 8, 488, 320, 23, 15, 481, 220, 22,
                            15, 8, 690, 9217, 29, 151645],
                            * [[8704, 582, 525, 3330, 369, 458, 23606, 429, 3059, 304, 220, 20, 24, 11, 323, 582, 2299, 7199, 311, 1667, 1817, 1372, 508, 22, 15, 11, 220,
                            22, 17, 11, 220, 23, 15, 11, 220, 17, 18, 60, 1172, 3055, 11, 279, 5795, 374, 311, 36635, 1493, 5109, 1526, 6770, 34784, 7525, 13, 3776,
                            3204, 1616, 311, 5486, 419, 374, 311, 1191, 448, 1045, 30339, 28117, 323, 1490, 421, 582, 646, 17331, 518, 220, 20, 24, 13, 6771, 594,
                            2908, 279, 3881, 5109, 323, 1430, 34171, 1105, 304, 2155, 5510, 13, 10696, 279, 6672, 1948, 1045, 5109, 686, 7540, 2494, 3265, 311, 220,
                            20, 24, 13, 6771, 594, 1430, 220, 23, 15, 481, 220, 17, 18, 311, 633, 220, 20, 22, 11, 1221, 1490, 421, 62514, 220, 22, 15, 323, 220, 22,
                            17, 686, 5545, 220, 20, 24, 13, 690, 26865, 397, 1654, 614, 220, 23, 15, 481, 220, 17, 18, 284, 220, 20, 22, 13, 1205, 1184, 311, 835, 705,
                            448, 220, 20, 24, 13, 4695, 11, 582, 1184, 311, 7500, 220, 20, 22, 311, 633, 311, 220, 20, 24, 13, 3776, 1616, 311, 653, 419, 374, 553,
                            1667, 220, 22, 17, 481, 220, 22, 15, 284, 220, 17, 13, 5005, 7842, 419, 220, 17, 311, 220, 20, 22, 686, 2968, 220, 20, 24, 13, 715, 10061,
                            594, 88859, 419, 510, 27, 9217, 29, 320, 23, 15, 481, 220, 17, 18, 8, 488, 320, 22, 17, 481, 220, 22, 15, 8, 690, 9217, 29, 151645]] * 2],
        'reasoning_steps': [['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59'], ['72', '72 - 23 = 49', '49 + 80 = 129', '129 - 70 = 59', '59']]
        }

    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import ModelConfig
    import torch



    model_config = ModelConfig(model_name_or_path='Qwen/Qwen2.5-0.5B-Instruct',
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


    for i, ids in enumerate(reward_inputs['completion_ids']):
        print("=" * 40 + f" {i} " + "=" * 40)
        thoughts, thought_ids_list = split_thoughts(
            completion_ids=ids,
            tokenizer=tokenizer,
            verbose=True
        )

    device = torch.device("cuda:5")
    model.to(device)

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
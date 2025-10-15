# %%
import torch
import numpy as np
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
COUNTDOWN = 6
PATH = "/nvme-data/jacob/Sys2Bench/outputs/Qwen2.5-3B-Instruct/citrinegui/Qwen2.5-3B-Instruct_countdown2345_grpo_vrex_0.25_0.75_SEC0.0DRO0.0G1.0_minpTrue_1600"
# %%
files = [os.path.join(PATH, f) for f in os.listdir(PATH) if f.endswith(".pt") if f"n{COUNTDOWN}t100" in f]
files
# %%
i = 3

file = files[i]
data = torch.load(file, map_location="cpu")
# %%
logProbsLs = data["logProbs"]
# %%
entropys = []
for promptGenerations in tqdm(logProbsLs):
    promptEntropys = []
    for generationLogits in promptGenerations:
        probs = torch.tensor(generationLogits).softmax(dim=-1)
        entropy = -(probs * probs.log()).sum(dim=-1)
        promptEntropys.append(entropy.tolist())
    entropys.append(promptEntropys)
# %%
# %%
newData = {'results': data["results"], 'entropys': entropys}
# %%
fileOut = file.replace(".pt", "_entropys.pt")
torch.save(newData, fileOut)
# %%

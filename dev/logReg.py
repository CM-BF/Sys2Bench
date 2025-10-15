# %%
import torch
import numpy as np
import os
from tqdm import tqdm
PATH = "/nvme-data/jacob/Sys2Bench/outputs/Qwen2.5-3B-Instruct/citrinegui/Qwen2.5-3B-Instruct_countdown2345_grpo_vrex_0.25_0.75_SEC0.0DRO0.0G1.0_minpTrue_1600"
# %%
COUNTDOWN = 6
files = [os.path.join(PATH, f) for f in os.listdir(PATH) if f.endswith(".pt") if f"n{COUNTDOWN}t100" in f and "entropys" in f]
files
# %%
dataUnjoined = [torch.load(f) for f in tqdm(files)]
# %%
dataJoined = {}
for k in dataUnjoined[0].keys():
    if k not in dataJoined:
        dataJoined[k] = []
    for d in dataUnjoined:
        dataJoined[k].extend(d[k])
# %%
dataJoined.keys()

# %%
labelsBatched = np.array(dataJoined["results"])
labelsBatched.shape
# %%
accuracies = labelsBatched.mean(axis=-1)
# %%
import matplotlib.pyplot as plt
plt.hist(accuracies, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Accuracy')
plt.ylabel('Frequency')
plt.title(f'Accuracies for Countdown {COUNTDOWN}')
plt.grid(axis='y', alpha=0.75)
plt.show()
# %%
accuraciesBatched = accuracies[:, None].repeat(labelsBatched.shape[-1], axis=-1)
accuraciesBatched.shape
accuraciesBatched
# %%
meanEntopiesLs = []
lastKEntropiesLs = []
minSeqLen = 1000
lastK = 100
for promptEntropy in dataJoined["entropys"]:
    for generationEntropy in promptEntropy:
        minSeqLen = min(minSeqLen, len(generationEntropy))        
        npEnt = np.array(generationEntropy)
        meanEnt = npEnt.mean().item()
        lastKEnt = npEnt[-lastK:].mean().item()
        meanEntopiesLs.append(meanEnt)
        lastKEntropiesLs.append(lastKEnt)

# %%
plt.hist(lastKEntropiesLs, bins=50, edgecolor='black', alpha=0.7)
plt.xlabel(f'Avg. Last {lastK} Token Entropy')
plt.ylabel('Frequency')
plt.title(f'Avg. Last {lastK} Token Entropies for Countdown {COUNTDOWN}')
plt.grid(axis='y', alpha=0.75)
plt.show()

# %%
accuracyLs = accuraciesBatched.flatten().tolist()
plt.scatter(meanEntopiesLs, accuracyLs)
# %%
plt.scatter(lastKEntropiesLs, accuracyLs, alpha=0.1)
# %%
labelsLs = labelsBatched.flatten().tolist()
len(labelsLs)
# %%
plt.bar(["Incorrect", "Correct"], [(labelsBatched == 0).sum(), (labelsBatched == 1).sum()], color=['red', 'green'], alpha=0.7)
plt.xlabel('Label')
plt.ylabel('Frequency')
plt.title(f'Label Distribution for Countdown {COUNTDOWN}')
plt.grid(axis='y', alpha=0.75)
plt.show()
# %%
import pandas as pd     
from statsmodels.formula.api import logit
import statsmodels.api as sm



# %%
df = pd.DataFrame({
    "accuracy": accuracyLs,
    "meanEntropy": meanEntopiesLs,
    f"last{lastK}Entropy": lastKEntropiesLs,
    "correct": labelsLs,
})
df = df[(df["accuracy"] != 1) & (df["accuracy"] != 0)]

df.head(10)
# %%
# %%
glm = logit(
    f"correct ~ last{lastK}Entropy + accuracy",
    df,
).fit()
TN, FP, FN, TP = glm.pred_table().flatten().tolist()
print(glm.summary())
print(f"Label counts:")
print(df["correct"].value_counts())
print("===============================================================================")
print(f"Accuracy counts:")
accuracy = (TP + TN) / (TP + TN + FP + FN)
correctAccuracy = TP / (TP + FN)
incorrectAccuracy = TN / (TN + FP)
print(f"Accuracy: {accuracy:.4f}\nCorrect accuracy: {correctAccuracy:.4f}\nIncorrect accuracy: {incorrectAccuracy:.4f}")
print("===============================================================================")
# %%
# TP, TN, FP, FN

# %%
# %%

# %%
predProbs = torch.sigmoid(torch.from_numpy(glm.fittedvalues.to_numpy()))
TP = ((predProbs >= 0.5) & (torch.tensor(df["correct"].to_numpy()) == 1)).sum().item()
TN = ((predProbs < 0.5) & (torch.tensor(df["correct"].to_numpy()) == 0)).sum().item()
FP = ((predProbs >= 0.5) & (torch.tensor(df["correct"].to_numpy()) == 0)).sum().item()
FN = ((predProbs < 0.5) & (torch.tensor(df["correct"].to_numpy()) == 1)).sum().item()
accuracy = (TP + TN) / (TP + TN + FP + FN)
accuracy
# %%
TP, TN, FP, FN
# %%

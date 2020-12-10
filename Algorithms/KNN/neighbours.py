import numpy as np
from math import sqrt
import warnings
from collections import Counter
import pandas as pd
import random 

#classifier
def k_nearest_neighbours(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to avalue less that total voting groups!')
    distances=[]
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]] # the first K neighbours
    vote_result = Counter(votes).most_common(1) [0][0]
    confidence = Counter(votes).most_common(1) [0][1] / k
    
    return vote_result, confidence

df = pd.read_csv("D:/_PROG/AI/PythonML/Classification/breast-cancer-wisconsin.data")
df.replace('?', -9999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))] # everything up to the last 20%
test_data = full_data[-int(test_size*len(full_data)):] # the last 20%

#sorting data in two sets (benign and mallignant)
for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0



for group in test_set:
    for data in test_set[group]:
        vote, confidence = k_nearest_neighbours(train_set, data, k=25)
        if group == vote:
            correct += 1
        else:
            print(confidence)
        total +=1

print(train_set[2][:5])
print("Accuracy: ", correct/total)
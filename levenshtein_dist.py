
import pandas as pd
import numpy as np

df = pd.read_csv('dog_names_dataset.csv')



def levenshtein_distance(source, target):
    """
    Assuming del cost = replace cost = insertion cost
    """
    l1, l2 = len(source), len(target)
    matrix = np.zeros((l2 + 1, l1 + 1))
    
    # insertion cost of empty source string to target string(first column of the matrix)
    for i in range(1, l1+1):
        matrix[0, i] += matrix[0, i-1] + 1
    # deletion cost of target string to empty string(first row of the matrix)
    for j in range(1, l2+1):
        matrix[j, 0] += matrix[j-1,0] + 1
            
    for j in range(1, l2+1):
        for i in range(1, l1+1):
            if source[i-1] == target[j-1]:
                
                matrix[j,i] = matrix[j-1, i-1]
                # print(matrix[j, i])
            else:
                a = min(matrix[j-1, i], matrix[j, i-1], matrix[j-1, i-1])
                matrix[j, i] = a + 1
                
    return int(matrix[l2, l1])
            


answer_list = []
for i in df['HUNDENAME'].tolist():
    dist = levenshtein_distance("Luca", i)
    if (dist == 1) and (i not in answer_list):
        answer_list.append(i)


import numpy as np


def bigram_counts(words):
    # Your code here
    string = ""
    for word in words:
        string += word
    single_val_set = set(string)
    # single_val_list =
    n = len(single_val_set)

    single_val_list = [char for char in single_val_set]
    single_val_list.sort()

    mem = {'.': 0}
    for i in range(n):
        mem[single_val_list[i]] = i+1

    mat = np.zeros((n+1, n+1))
    for word in words:
        if len(word) == 1:
            mat[0, mem[word]] += 1
            mat[mem[word], 0] += 1
            continue

        mat[0, mem[word[0]]] += 1
        for i in range(len(word)-1):
            mat[mem[word[i]], mem[word[i+1]]] += 1

        mat[mem[word[-1]], 0] += 1
    return mat

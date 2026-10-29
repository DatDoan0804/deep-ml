import numpy as np


def bigram_counts(words):

    vocab = ["."] + sorted({char for word in words for char in word})
    vocab_size = len(vocab)
    stoi = {char: index for index, char in enumerate(vocab)}

    mat = np.zeros((vocab_size, vocab_size))
    for word in words:
        token = "."+word+"."

        for i in range(len(token)-1):
            mat[stoi[token[i]], stoi[token[i+1]]] += 1

    return mat

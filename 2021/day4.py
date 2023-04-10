#!/usr/local/bin/python3
from collections import OrderedDict


def findWinnerScore(numbers, B):
    S = [0] * len(B)
    for k in range(len(B)):
        for i in range(5):
            for j in range(5):
                S[k] += B[k][i][j]
    W = OrderedDict()
    for n in numbers:
        for k in range(len(B)):
            for i in range(5):
                for j in range(5):
                    if B[k][i][j] == n:
                        S[k] -= B[k][i][j]
                        B[k][i][j] = -1
                        S1 = set(B[k][ii][j] for ii in range(5))
                        S2 = set(B[k][i][jj] for jj in range(5))
                        if (S1 == set([-1]) or S2 == set([-1])) and k not in W:
                            W[k] = n * S[k]
    return list(W.values())


numbers = []
B = []
with open('day4.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if not numbers:
            numbers = list(map(int, line.split(',')))
            continue
        line = line.strip()
        if line == '':
            B += [[]]
        else:
            B[-1] += [list(map(int, line.split()))]

H = findWinnerScore(numbers, B)
print('First solution:', H[0])
print('Second solution:', H[-1])

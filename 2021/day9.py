#!/usr/local/bin/python3
'''
Advent of code day 9
'''
from collections import defaultdict
# TODO FIXME: second part

# ---
M = []
with open('day9a.txt', 'r', encoding='ascii') as f:
    while True:
        line = f.readline()
        if not line:
            break
        M += [list(map(int, list(line.strip())))]

X, Y = len(M), len(M[0])
SCORE = 0
sink = set()
D = defaultdict(set)
for i in range(X):
    for j in range(Y):
        N = []
        CNT = 0
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            x, y = i + dx, j + dy
            if 0 <= x < X and 0 <= y < Y:
                N += [M[x][y]]
                if M[x][y] > M[i][j]:
                    CNT += 1
                    if M[x][y] != 9:
                        D[f'({i},{j})'].add(f'({x},{y}:{M[x][y]})')
        if len(N) == CNT:
            SCORE += 1 + M[i][j]
            sink.add(f'({i},{j})')
print('First solution:', SCORE)

for si in D:
    print(si, D[si])

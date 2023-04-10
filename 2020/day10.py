#!/usr/local/bin/python3


# FILE = 'day10b.txt'
# FILE = 'day10a.txt'
FILE = 'day10.txt'
S = []
M = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        v = int(line.strip())
        M = max(M, v)
        S.append(v)
S.append(0)
S.append(M + 3)
S.sort()
H = {1: 0, 3: 0}
for i in range(1, len(S)):
    H[S[i] - S[i-1]] += 1
print('First answer:', H[1]*H[3])

A = {0: 1}
for i in range(1, len(S)):
    v = 0
    for j in range(1, 4):
        if S[i] - j in S:
            v += A[S[i] - j]
    A[S[i]] = v
print('Second answer:', A[S[-1]])

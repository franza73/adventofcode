#!/usr/local/bin/python3


N = 2020
s = list()
with open('input1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        n = int(line.strip())
        s += [n]

L = len(s)
for i in range(L):
    for j in range(i+1, L):
        d = 2020 - (s[i] + s[j])
        if d in s:
            print(s[i] * s[j] * d)
            break

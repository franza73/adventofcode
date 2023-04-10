#!/usr/local/bin/python3
from collections import Counter


def iterate(initial_state, n_iter):
    d_0 = Counter(initial_state)
    for _ in range(n_iter):
        d_1 = Counter()
        for k in d_0:
            if k > 0:
                d_1[k-1] += d_0[k]
            else:
                d_1[8] = d_0[0]
                d_1[6] += d_0[0]
        d_0 = Counter(d_1)
    res = 0
    for k in d_0:
        res += d_0[k]
    return res


p = []
with open('day6.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        p = list(map(int, line.strip().split(',')))


print('First solution:', iterate(p, 80))
print('Second solution:', iterate(p, 256))

#!/usr/local/bin/python3
from collections import deque


# W, FILE = 5, 'day9.txt'
W, FILE = 25, 'day9a.txt'
w = deque()
L = []
i = 0
fn = True
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        s = line.strip()
        s = int(s)
        if i < W:
            w.append(s)
        else:
            if not any(s - wi in w for wi in w) and fn:
                FN = s
                print('First number:', s)
                fn = False
            w.popleft()
            w.append(s)
        L.append(s)
        i += 1

# -- second part --
w.clear()
S = 0
for Li in L:
    if S < FN:
        S += Li
        w.append(Li)
    elif S == FN:
        print('Second number:', min(w) + max(w))
        break
    while S > FN and w:
        Si = w.popleft()
        S -= Si

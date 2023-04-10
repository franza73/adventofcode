#!/usr/local/bin/python3
from collections import Counter


# FILE = 'day21a.txt'
FILE = 'day21b.txt'
H = {}
CNT = Counter()
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().replace(')', '').split(' (contains ')
        sl = line[0].split(' ')
        CNT += Counter(sl)
        S = set(sl)
        for item in line[1].split(', '):
            if item not in H:
                H[item] = S
            else:
                H[item] = H[item].intersection(S)
bound = set()
LOOP = True
r = []
while LOOP:
    LOOP = False
    for item in H:
        intersect = H[item].difference(bound)
        ln = len(intersect)
        if ln == 1:
            v = intersect.pop()
            r += [(item, v)]
            bound.add(v)
        elif ln > 1:
            LOOP = True
print('First answer:', sum(CNT[i] for i in CNT if i not in bound))
r.sort()
print('Second answer:', ','.join(ri for _, ri in r))

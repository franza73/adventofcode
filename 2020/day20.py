#!/usr/local/bin/python3
from collections import Counter
import re


def rh(s):
    return '\n'.join(reversed(s.splitlines()))


def rv(s):
    return '\n'.join(map(lambda s: s[::-1], s.splitlines()))


def rhv(s):
    return rv(rh(s))


def flip(s):
    ls = s.splitlines()
    L = len(ls[0])
    M = len(ls)
    r = ['' for _ in range(L)]
    for i in range(L):
        for j in range(M):
            r[i] += ls[j][i]
    return rv('\n'.join(r))


def rotPlus90(s):
    return flip(s)


def rotMinus90(s):
    return rhv(flip(s))


FILE = 'day20a.txt'
FILE = 'day20b.txt'
H = {}
# Count the number of corners that are unmatched
CNT = Counter()
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        m = re.search(r'Tile (\d+)', line)
        if m:
            tile = m.group(1)
            i = 0
            a, b, c, d = '', '', '', ''
        elif re.search(r'^\s*$', line):
            H[tile] = []
            for k in [a, b, c, d]:
                key = sorted([k, k[::-1]])[0]
                CNT[key] += 1
                H[tile] += [k]
        else:
            if i == 0:
                a = line
            elif i == 9:
                c = line
            b += line[9]
            d += line[0]
            i += 1
# Corner image squares will have two unmatched edges
prod = 1
UL = ''
for tile in H:
    cnt = 0
    for corner in H[tile]:
        if CNT[corner] == 1 or CNT[corner[::-1]] == 1:
            cnt += 1
    if cnt == 2:
        prod *= int(tile)
        if not UL:
            UL = tile
print('First answer:', prod)
#
# 1. Put together the complete image
# 2. For each possible rotation of the dragon,
#    find them inside the image

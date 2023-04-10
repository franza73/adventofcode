#!/usr/local/bin/python3
import re


def numberOfOverlaps(P, method):
    D = {}
    cnt = 0
    for x1, y1, x2, y2 in P:
        if x1 == x2:
            for k in range(min(y1, y2), max(y1, y2)+1):
                K = f'({x1},{k})'
                if K not in D:
                    D[K] = 1
                else:
                    D[K] += 1
        elif y1 == y2:
            for k in range(min(x1, x2), max(x1, x2)+1):
                K = f'({k},{y1})'
                if K not in D:
                    D[K] = 1
                else:
                    D[K] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            if method == 'first':
                continue
            if x2 > x1:
                Rx = range(x1, x2 + 1)
            else:
                Rx = range(x1, x2 - 1, -1)
            if y2 > y1:
                Ry = range(y1, y2 + 1)
            else:
                Ry = range(y1, y2 - 1, -1)
            for x, y in zip(Rx, Ry):
                K = f'({x},{y})'
                if K not in D:
                    D[K] = 1
                else:
                    D[K] += 1
        else:
            raise Exception('Unexpected input')
    for k in D:
        if D[k] > 1:
            cnt += 1
    return cnt


P = []
with open('day5.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        x1, y1, x2, y2 = map(int, re.split(r'\D+', line.strip()))
        P += [(x1, y1, x2, y2)]

print('First solution:', numberOfOverlaps(P, 'first'))
print('Second solution:', numberOfOverlaps(P, 'second'))

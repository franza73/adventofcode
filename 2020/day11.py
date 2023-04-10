#!/usr/local/bin/python3
from copy import deepcopy


# FILE = 'day11a.txt'
FILE = 'day11b.txt'
# -- read matrix --
m = []
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        m += [list(line.strip())]
X = len(m)
Y = len(m[0])
D = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]


def next_iter_1(m):
    n = deepcopy(m)
    for i in range(X):
        for j in range(Y):
            if m[i][j] == '.':
                continue
            busy_adj = 0
            for dx, dy in D:
                x = i + dx
                y = j + dy
                if 0 <= x < X and 0 <= y < Y and m[x][y] == '#':
                    busy_adj += 1
            if m[i][j] == 'L' and busy_adj == 0:
                n[i][j] = '#'
            if m[i][j] == '#' and busy_adj >= 4:
                n[i][j] = 'L'
    return n


def next_iter_2(m):
    n = deepcopy(m)
    for i in range(X):
        for j in range(Y):
            if m[i][j] == '.':
                continue
            busy_adj = 0
            for dx, dy in D:
                x = i + dx
                y = j + dy
                while 0 <= x < X and 0 <= y < Y:
                    if m[x][y] == '#':
                        busy_adj += 1
                        break
                    elif m[x][y] == 'L':
                        break
                    x += dx
                    y += dy
            if m[i][j] == 'L' and busy_adj == 0:
                n[i][j] = '#'
            if m[i][j] == '#' and busy_adj >= 5:
                n[i][j] = 'L'
    return n


def equal(m, n):
    for i in range(X):
        for j in range(Y):
            if m[i][j] != n[i][j]:
                return False
    return True


def busy(m):
    cnt = 0
    for i in range(X):
        for j in range(Y):
            if m[i][j] == '#':
                cnt += 1
    return cnt


def steady(m, next_iter):
    while True:
        n = next_iter(m)
        if equal(m, n):
            break
        m = deepcopy(n)
    return m


print('First answer:', busy(steady(m, next_iter_1)))
print('Second answer:', busy(steady(m, next_iter_2)))

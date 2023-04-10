#!/usr/local/bin/python3


# -- read into matrix --
m = []
with open('day3b.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        m += [list(line.strip())]
X = len(m)
Y = len(m[0])

# -- follow the direction --
d = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
prod = 1
for dx, dy in d:
    cnt = 0
    x, y = 0, 0
    while True:
        x += dx
        y += dy
        y %= Y
        if x >= X:
            break
        if m[x][y] == '#':
            cnt += 1
    prod *= cnt
print(prod)

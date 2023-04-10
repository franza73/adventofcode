#!/usr/local/bin/python3


# -- consts --
D3 = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2)
      for z in range(-1, 2) if (x, y, z) != (0, 0, 0)]
D4 = [(x, y, z, w) for x in range(-1, 2) for y in range(-1, 2)
      for z in range(-1, 2) for w in range(-1, 2)
      if (x, y, z, w) != (0, 0, 0, 0)]


'''
def _print_(s):
    for z in range(B[2][0], B[2][1] + 1):
        for x in range(B[0][0], B[0][1] + 1):
            for y in range(B[1][0], B[1][1] + 1):
                if (x, y, z) in s:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()
'''


def _add_(active, v):
    global B
    B = [[min(B[i][0], vi), max(B[i][1], vi)] for i, vi in enumerate(v)]
    active.add(v)


def _neighs_(v):
    if DIM == 3:
        x, y, z = v
        r = []
        for dx, dy, dz in D3:
            r += [(x+dx, y+dy, z+dz)]
        return r
    elif DIM == 4:
        x, y, z, w = v
        r = []
        for dx, dy, dz, dw in D4:
            r += [(x+dx, y+dy, z+dz, w+dw)]
        return r


def _next_(active):
    global B
    inactive = set()
    new_active = set()
    B = [[100, -100] for _ in range(DIM)]
    for v in active:
        cnt = 0
        for vi in _neighs_(v):
            if vi in active:
                cnt += 1
            else:
                inactive.add(vi)
        if cnt == 2 or cnt == 3:
            _add_(new_active, v)
    for v in inactive:
        cnt = 0
        for vi in _neighs_(v):
            if vi in active:
                cnt += 1
        if cnt == 3:
            _add_(new_active, v)
    return new_active


# -- read the matrix --
# FILE = 'day17a.txt'
FILE = 'day17b.txt'
DIM = 3
B = [[100, -100] for _ in range(DIM)]
active = set()
i = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        for j, v in enumerate(list(line.strip())):
            if v == '#':
                _add_(active, (i, j, 0))
        i += 1

# -- iterations --
for _ in range(6):
    active = _next_(active)
print('First answer:', len(active))

# -- read the matrix --
DIM = 4
B = [[100, -100] for _ in range(DIM)]
active = set()
i = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        for j, v in enumerate(list(line.strip())):
            if v == '#':
                _add_(active, (i, j, 0, 0))
        i += 1

# -- iterations --
for _ in range(6):
    active = _next_(active)
print('Second answer:', len(active))

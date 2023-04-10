#!/usr/local/bin/python3


def seat_id(s):
    L, R = 0, 127
    for i in range(7):
        M = (L + R) // 2
        if s[i] == 'F':
            R = M
        elif s[i] == 'B':
            L = M + 1
    assert(L == R)
    v = L
    L, R = 0, 7
    for i in range(7, 10):
        M = (L + R) // 2
        if s[i] == 'R':
            L = M + 1
        elif s[i] == 'L':
            R = M
    assert(L == R)
    v = v*8 + L
    return v


m, M = 0, 0
S = set()
with open('day5a.txt', 'r') as f:
    while True:
        line = f.readline()
        s = line.strip()
        if not line:
            break
        s = line.strip()
        v = seat_id(s)
        M = max(M, v)
        m = min(m, v)
        S.add(v)

print('First answer:')
print(M)
print('Second answer:')
for si in range(m, M+1):
    if si not in S:
        if (si == m):
            if si + 1 in S:
                print(si)
        elif si - 1 in S and si + 1 in S:
            print(si)

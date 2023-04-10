#!/usr/bin/env python3


def dest(p, t, M):
    while True:
        p -= 1
        if p == 0:
            p = M
        if p not in t:
            return p


def move(a, M, n, fmt='first'):
    # create the circular data structure
    N = {}
    ai = a[0]
    for bi in a[1:]:
        N[ai] = bi
        ai = bi
    La = len(a)
    if La == M:
        N[a[-1]] = a[0]
    else:
        N[a[-1]] = La+1
        for i in range(La+1, M):
            N[i] = i+1
        N[M] = a[0]
    # simulate moves
    p = a[0]
    for _ in range(n):
        t = [N[p], N[N[p]], N[N[N[p]]]]
        N[p] = N[t[-1]]
        d = dest(p, t, M)
        N[t[-1]] = N[d]
        N[d] = t[0]
        # new 'p'
        p = N[p]
    if fmt == 'first':
        v = 1
        s = ''
        for _ in range(len(N)-1):
            s += str(N[v])
            v = N[v]
        return s
    else:
        return N[1] * N[N[1]]


# -- test --
# a = list(map(int, list('389125467')))
# -- input --
a = list(map(int, list('476138259')))
print('First answer:', move(a, len(a), 100))
print('Second answer:', move(a, 1000000, 10000000, fmt='second'))

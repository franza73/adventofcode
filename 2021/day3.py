#!/usr/local/bin/python3


def histogram(L):
    if len(L) == 0:
        raise Exception('Empty list for histogram')
    lc = len(L[0])
    N = 0
    C = []
    for li in L:
        if N == 0:
            C = [0] * lc
        for i in range(lc):
            C[i] += li[i]
        N += 1
    return C, N


def powerConsumption(L):
    C, N = histogram(L)
    a, b = 0, 0
    sz = len(C)
    for i in range(sz):
        if C[i] > N // 2:
            a += 2**(sz-i-1)
        elif C[i] < N // 2:
            b += 2**(sz-i-1)
        else:
            raise Exception('Unexpected!')
    return a * b


def lifeSupportRating(L):
    def toNum(V):
        lv = len(V)
        res = 0
        for i in range(lv):
            res += 2**(lv-i-1) * V[i]
        return res

    def rate(L, rating):
        if rating not in set(['oxygen', 'co2']):
            raise Exception('Invalid rating type')
        b = 0
        while len(L) > 1:
            C, N = histogram(L)
            N1, N0 = C[b], N - C[b]
            if rating == 'oxygen':
                v = (N1 >= N0)
            else:
                v = (N1 < N0)
            L = list(filter(lambda x: x[b] == v, L))
            b += 1
        return toNum(L[0])

    return rate(L, 'oxygen') * rate(L, 'co2')


data = []
with open('day3b.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        data += [list(map(int, line.strip()))]

print('First solution:', powerConsumption(data))
print('Second solution:', lifeSupportRating(data))

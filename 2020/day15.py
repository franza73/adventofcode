#!/usr/local/bin/python3


def simulate(v, N):
    last_index = {k: v for v, k in enumerate(v[:-1], 1)}
    current = v[-1]
    for k in range(len(v) + 1, N + 1):
        if current not in last_index:
            key = 0
        else:
            key = k - 1 - last_index[current]
        last_index[current] = k - 1
        current = key
    return current


v = [8, 13, 1, 0, 18, 9]

print('First answer:', simulate(v, 2020))
print('Second answer:', simulate(v, 30000000))

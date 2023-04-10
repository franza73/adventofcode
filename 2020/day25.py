#!/usr/bin/env python3


def find_index(S):
    V1 = 1
    i = 1
    while True:
        V1 *= 7
        V1 %= M
        if V1 == S:
            return i
        i += 1


# -- init --
M = 20201227
V1 = 1
H1 = {}
V2 = 1
H2 = {}

# -- test --
# S1 = 17807724
# S2 = 5764801

# -- validate --
S1 = 10943862
S2 = 12721030

N1 = find_index(S1)
N2 = find_index(S2)

for i in range(1, 1 + N2):
    V1 *= S1
    V1 %= M
for i in range(1, 1 + N1):
    V2 *= S2
    V2 %= M
assert(V1 == V2)
print('First answer:', V1)

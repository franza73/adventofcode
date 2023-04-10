#!/usr/local/bin/python3
import re


# -- read input into dict --
H = {}
with open('day7b.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        s = line.strip()
        s = s.replace(' contain ', '')
        v = re.split(r' bags?[,.]?\s?', s)[:-1]
        m = v[1:]
        if m != ['no other']:
            H[v[0]] = {k: int(v) for v, k in map(lambda s: s.split(' ', 1), m)}


def contain_shiny_gold(s):
    if s not in H:
        return False
    elif 'shiny gold' in H[s]:
        return True
    else:
        for k in H[s].keys():
            if contain_shiny_gold(k):
                return True
    return False


def calculate(s):
    if s not in H:
        return 1
    else:
        return 1 + sum(calculate(k)*v for k, v in H[s].items())


# -- for each key, recursively resolve until 'no other' --
cnt = 0
for k in H.keys():
    if contain_shiny_gold(k):
        cnt += 1

print('First  answer:', cnt)

print('Second answer:', calculate('shiny gold') - 1)

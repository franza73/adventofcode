#!/usr/local/bin/python3
import re


def valid_rules(x):
    for r in rules:
        if r[0] <= x <= r[1] or r[2] <= x <= r[3]:
            return True
    return False


def matches_rules(x):
    x = int(x)
    if x in MEM:
        return MEM[x]
    st = set()
    for i, r in enumerate(rules):
        if r[0] <= x <= r[1] or r[2] <= x <= r[3]:
            st.add(i)
    MEM[x] = st
    return st


# FILE = 'day16a.txt'
FILE = 'day16b.txt'
# FILE = 'day16c.txt'
MEM = {}
PHASE = 0
rules = []
valid = []
cnt = 0
mine = []
rule_names = []
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        v = line.strip().split(':')
        if v[0] == 'your ticket':
            PHASE = 1
        elif v[0] == 'nearby tickets':
            PHASE = 2
        elif PHASE == 0 and len(v) == 2:
            rules += [list(map(int, re.split(r'\D+', v[1].strip())))]
            rule_names += [v[0]]
        elif PHASE == 1:
            if ',' in v[0]:
                mine = v[0].split(',')
        elif PHASE == 2:
            isValid = True
            for vi in v[0].split(','):
                vi = int(vi)
                if not valid_rules(vi):
                    cnt += vi
                    isValid = False
            if isValid:
                valid += [v[0].split(',')]
print('First answer:', cnt)
# D[index] -> which rules are feasible
D = [matches_rules(vii) for vii in valid[0]]
for vi in valid[1:]:
    for i, vii in enumerate(vi):
        D[i] = D[i].intersection(matches_rules(vii))
lst = sorted((len(di), i, di) for i, di in enumerate(D))
S = set()
prod = 1
for _, _index, _rules in lst:
    _rules = {i for i in _rules if i not in S}
    if len(_rules) == 1:
        S.update(_rules)
    else:
        print('ERROR: Not ready for this!')
        exit(-1)
    if re.search(r'^departure', rule_names[_rules.pop()]):
        prod *= int(mine[_index])
print('Second answer:', prod)

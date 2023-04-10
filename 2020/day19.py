#!/usr/local/bin/python3
import re


def match(rule, s):
    if R[rule] == 'a' or R[rule] == 'b':
        if len(s) < 1 or s[0] != R[rule]:
            return [None]
        else:
            return [s[1:]]
    else:
        res = []
        rules = R[rule].split('|')
        for r in rules:
            r = list(map(int, r.split()))
            v = [s]
            for ri in r:
                vv = []
                for vi in v:
                    vv.extend([si for si in match(ri, vi) if si is not None])
                v = list(vv)
            res.extend(v)
        return res


# -- read the input --
R = {}
S = []
# FILE = 'day19a.txt'
FILE = 'day19b.txt'
# FILE = 'day19c.txt'
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        m = re.search(r'(\d+): "?([^"]+)"?', line)
        if m:
            R[int(m.group(1))] = m.group(2)
        elif line != '':
            S += [line]

# -- results --
print('First answer:', sum('' in match(0, s) for s in S))

R[8] = '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42'
R[11] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31'
# TODO FIXME: The correct approach would be to add new items to rules list in
# case of 'recursive' option (8, 11). This only needs to be done until
# the v returns empty.
print('Second answer:', sum('' in match(0, s) for s in S))

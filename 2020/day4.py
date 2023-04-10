#!/usr/local/bin/python3
import re


def is_valid_field(key, val):
    if key == 'byr' and (not 1920 <= int(val) <= 2002 or len(val) != 4):
        return False
    elif key == 'iyr' and (not 2010 <= int(val) <= 2020 or len(val) != 4):
        return False
    elif key == 'eyr' and (not 2020 <= int(val) <= 2030 or len(val) != 4):
        return False
    elif key == 'hgt':
        if 'cm' in val:
            val = val.replace('cm', '')
            if not 150 <= int(val) <= 193:
                return False
        elif 'in' in val:
            val = val.replace('in', '')
            if not 59 <= int(val) <= 76:
                return False
        else:
            return False
    elif key == 'hcl' and not re.search(r'^#[0-9a-f]{6}$', val):
        return False
    elif key == 'ecl' and val not in S:
        return False
    elif key == 'pid' and not re.search(r'^\d{9}$', val):
        return False
    return True


def is_valid(v):
    for key, val in v.items():
        if not is_valid_field(key, val):
            return False
    return True


K1 = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
K2 = K1.union(set(['cid']))
S = set('amb blu brn gry grn hzl oth'.split())
v = dict()
cnt = 0
with open('day4b.txt', 'r') as f:
    while True:
        line = f.readline()
        s = line.strip()
        if not line:
            break
        s = line.strip()
        if re.search(r'^\s*$', s):
            keys = v.keys()
            if keys == K1 or keys == K2:
                if is_valid(v):
                    cnt += 1
            v = dict()
        else:
            si = s.split()
            for sii in si:
                key, val = sii.split(':')
                v[key] = val
print(cnt)

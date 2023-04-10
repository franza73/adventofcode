#!/usr/local/bin/python3
import re


v = set()
cnt = 0
NEW = True
with open('day6b.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        s = line.strip()
        if re.search(r'^\s*$', s):
            cnt += len(v)
            v = set()
            NEW = True
        else:
            if NEW:
                v.update(list(s))
                NEW = False
            else:
                v = v.intersection(list(s))
print(cnt)

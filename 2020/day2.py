#!/usr/local/bin/python3
import re

cnt = 0
with open('day2.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        m = re.search(r'^(\d+)-(\d+)\s+(\S):\s+(\S+)', line.strip())
        if m:
            v1, v2, c, s = m.groups()
            # if int(v1) <= s.count(c) <= int(v2):
            #     cnt += 1
            if (s[int(v1) - 1] == c and s[int(v2) - 1] != c) or \
               (s[int(v1) - 1] != c and s[int(v2) - 1] == c):
                cnt += 1
        else:
            print('ERROR')
            break
print(cnt)

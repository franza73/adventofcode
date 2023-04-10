#!/usr/local/bin/python3
'''
Advent od code day 1
'''
from collections import deque


i = 0
cnt_1, cnt_2 = 0, 0
m_1, n_1 = 0, 0
q = deque()
with open('day1.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        n = int(line.strip())
        # first counter
        if i > 0 and n > n_1:
            cnt_1 += 1
        n_1 = n
        # second counter
        q.append(n)
        if i < 3:
            m_1 += n
        else:
            m = m_1 + n - q.popleft()
            if m > m_1:
                cnt_2 += 1
            m_1 = m
        i += 1

print('First solution:', cnt_1)
print('Second solution:', cnt_2)

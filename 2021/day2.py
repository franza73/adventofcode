#!/usr/local/bin/python3
'''
Advent of code day 2
'''


dep, hor = 0, 0
a, d, h = 0, 0, 0
with open('day2.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        cmd, n = line.strip().split()
        n = int(n)
        if cmd == 'forward':
            hor += n
            h += n
            d += a*n
        elif cmd == 'down':
            dep += n
            a += n
        elif cmd == 'up':
            dep -= n
            a -= n
        else:
            raise Exception('Unexpected input')
print('First solution:', dep*hor)
print('Second solution:', d*h)

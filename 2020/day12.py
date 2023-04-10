#!/usr/local/bin/python3
from math import sqrt


# FILE = 'day12a.txt'
FILE = 'day12b.txt'
x, y = 0, 0
Di = 0
D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        cmd, val = line[0], int(line[1:])
        if cmd == 'F':
            dx, dy = D[Di]
            x += (dx*val)//sqrt(dx**2 + dy**2)
            y += (dy*val)//sqrt(dx**2 + dy**2)
        elif cmd == 'N':
            y += val
        elif cmd == 'S':
            y -= val
        elif cmd == 'E':
            x += val
        elif cmd == 'W':
            x -= val
        elif cmd == 'R':
            Di = (Di + val//90) % 4
        elif cmd == 'L':
            Di = (Di - val//90) % 4
print('First answer:', int(abs(x) + abs(y)))


wpx, wpy = 10, 1
x, y = 0, 0
Di = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        cmd, val = line[0], int(line[1:])
        if cmd == 'F':
            x += val * wpx
            y += val * wpy
        elif cmd == 'N':
            wpy += val
        elif cmd == 'S':
            wpy -= val
        elif cmd == 'E':
            wpx += val
        elif cmd == 'W':
            wpx -= val
        elif cmd == 'R' or cmd == 'L':
            if cmd == 'R':
                sign = 1
            else:
                sign = -1
            Di = (sign * val//90) % 4
            wpx, wpy = [(wpx, wpy), (wpy, -wpx), (-wpx, -wpy), (-wpy, wpx)][Di]
print('Second answer:', int(abs(x) + abs(y)))

#!/usr/local/bin/python3


def maskme(v, mask):
    r = 0
    p = 1
    for i in range(36):
        if mask[i] == 'X':
            r += v & p
        elif mask[i] == '1':
            r += p
        p <<= 1
    return r


def maskaddress(address, mask):
    r, p = '', 1
    for i in range(36):
        if mask[i] == '0':
            r += str((address & p) >> i)
        else:
            r += mask[i]
        p <<= 1
    l1 = [r]
    while True:
        l2 = []
        for li in l1:
            if 'X' not in li:
                continue
            for i in range(2):
                l2 += [li.replace('X', str(i), 1)]
        if not l2:
            break
        l1 = list(l2)
    return list(map(lambda x: int(x, 2), l1))


# FILE = 'day14a.txt'
FILE = 'day14b.txt'
# FILE = 'day14c.txt'
MEM = {}
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        v = line.strip().split(' = ')
        if v[0] == 'mask':
            mask = v[1][::-1]
        else:
            address = int(v[0].replace('mem[', '').replace(']', ''))
            MEM[address] = maskme(int(v[1]), mask)
print('First answer:', sum(MEM.values()))

MEM = {}
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        v = line.strip().split(' = ')
        if v[0] == 'mask':
            mask = v[1][::-1]
        else:
            BASE = int(v[0].replace('mem[', '').replace(']', ''))
            for address in maskaddress(BASE, mask):
                MEM[address] = int(v[1])
print('Second answer:', sum(MEM.values()))

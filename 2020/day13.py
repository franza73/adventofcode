#!/usr/local/bin/python3
'''
Basic application of the Chinese Remainder Theorem
'''
from sympy.ntheory.modular import crt


# FILE = 'day13a.txt'
FILE = 'day13b.txt'
with open(FILE, 'r') as f:
    n0 = int(f.readline())
    v = f.readline().split(',')
    buses = [int(vi) for vi in v if vi != 'x']
    residues = [-i for i, vi in enumerate(v) if vi != 'x']

n = n0
loop = True
while True:
    for bi in buses:
        if n % bi == 0:
            loop = False
            break
    if not loop:
        break
    n += 1
print('First answer:', (n-n0)*bi)

print('Second answer:', crt(buses, residues)[0])

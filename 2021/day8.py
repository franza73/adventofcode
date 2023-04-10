#!/usr/local/bin/python3
'''
Advent of code day 8
'''
from collections import defaultdict


def _to_hash(l_i):
    return ''.join(sorted(l_i))


def decode(numbers):
    '''
    Decode the numbers
    '''
    sz_to_set = defaultdict(list)
    set_to_number = {}
    for n_i in numbers.split():
        sz_to_set[len(n_i)] += [set(n_i)]
    set_to_number[_to_hash(sz_to_set[2][0])] = 1
    set_to_number[_to_hash(sz_to_set[3][0])] = 7
    set_to_number[_to_hash(sz_to_set[4][0])] = 4
    set_to_number[_to_hash(sz_to_set[7][0])] = 8
    for n_i in sz_to_set[5]:
        if len(sz_to_set[2][0].intersection(n_i)) == 2:
            set_to_number[_to_hash(n_i)] = 3
        elif len(sz_to_set[4][0].intersection(n_i)) == 3:
            set_to_number[_to_hash(n_i)] = 5
        else:
            set_to_number[_to_hash(n_i)] = 2
    for n_i in sz_to_set[6]:
        if len(sz_to_set[2][0].intersection(n_i)) == 1:
            set_to_number[_to_hash(n_i)] = 6
        elif len(sz_to_set[4][0].intersection(n_i)) == 4:
            set_to_number[_to_hash(n_i)] = 9
        else:
            set_to_number[_to_hash(n_i)] = 0
    return set_to_number


easy_lengths = set([2, 3, 4, 7])
CNT_1 = 0
CNT_2 = 0
with open('day8.txt', 'r', encoding='ascii') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = list(map(lambda x: x.strip(), line.split('|')))
        DECODE = decode(line[0])

        # calculate results
        NUMBER = 0
        for x in line[1].split():
            value = len(x)
            if value in easy_lengths:
                CNT_1 += 1
            NUMBER = NUMBER*10 + DECODE[_to_hash(set(x))]
        CNT_2 += NUMBER

print('First solution:', CNT_1)
print('Second solution:', CNT_2)

#!/usr/local/bin/python3
'''
Advent of code day7
'''


def median_even(data):
    '''
    Calculate the median of 'data'
    '''
    data = sorted(data)
    l_data = len(data)
    if l_data % 2 != 0:
        raise Exception('Need even sized data')
    p_data = l_data // 2
    median = (data[p_data-1] + data[p_data]) // 2
    return sum(map(lambda x: abs(x - median), data))


def fuel_amount(data):
    '''
    Find best fuel amount
    '''
    def _sum_(value):
        return (value*(value+1))//2

    def _amount(data, average):
        return sum(map(lambda x: _sum_(abs(x - average)), data))

    l_data = len(data)
    average = int(sum(data) / l_data)
    return min(_amount(data, average), _amount(data, average + 1))


p = []
with open('day7.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        p = list(map(int, line.strip().split(',')))

print('First solution:', median_even(p))
print('Second solution:', fuel_amount(p))

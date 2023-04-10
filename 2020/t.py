#!/usr/local/bin/python3

# day 20 


def rh(s):
    return '\n'.join(reversed(s.splitlines()))


def rv(s):
    return '\n'.join(map(lambda s: s[::-1], s.splitlines()))


def rhv(s):
    return rv(rh(s))


def rot(s):
    ls = s.splitlines()
    L = len(ls[0])
    M = len(ls)
    r = ['' for _ in range(L)]
    for i in range(L):
        for j in range(M):
            r[i] += ls[j][i]
    return rv('\n'.join(r))


s = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

s = '''  #
###'''
'''
print(s)
print()
print(rh(s))
print()
print(rv(s))
print()
print(rhv(s))
print()
s = rot(s)
print(s)
print()
print(rh(s))
print()
print(rv(s))
print()
print(rhv(s))
'''
def rotPlus90(s):
    return rot(s)
def rotMinus90(s):
    return rhv(rot(s))
print(s)
print()
print(rotPlus90(s))
print()
print(rotMinus90(s))

#!/usr/local/bin/python3


# FILE = 'day18a.txt'
FILE = 'day18b.txt'
total_sum = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        q = []
        line = line.strip().replace(' ', '')
        for v in list(line):
            q.append(v)
            doIt = True
            while doIt:
                doIt = False
                while len(q) > 2 and q[-1] not in '()' and q[-2] not in '()' \
                        and q[-3] not in '()':
                    a = int(q.pop())
                    op = q.pop()
                    b = int(q.pop())
                    if op == '+':
                        q.append(str(a + b))
                    elif op == '*':
                        q.append(str(a * b))
                    doIt = True
                while len(q) > 2 and q[-1] == ')' and q[-3] == '(':
                    q.pop()
                    v = q.pop()
                    q.pop()
                    q.append(v)
                    doIt = True
        total_sum += int(q.pop())
print('First answer:', total_sum)
total_sum = 0
with open(FILE, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        q = []
        line = line.strip().replace(' ', '')
        for v in list(line):
            q.append(v)
            doIt = True
            while doIt:
                doIt = False
                while len(q) > 2 and q[-1] not in '()' and q[-2] == '+' \
                        and q[-3] not in '()':
                    a = int(q.pop())
                    op = q.pop()
                    b = int(q.pop())
                    q.append(str(a + b))
                    doIt = True
                if len(q) > 2 and q[-1] == ')':
                    q.pop()
                    prod = 1
                    while True:
                        v = q.pop()
                        if v == '(':
                            break
                        elif v == '*':
                            continue
                        assert(v != '+')
                        prod *= int(v)
                    q.append(str(prod))
                    doIt = True
        while len(q) > 2 and q[-1] not in '()' and q[-2] == '*' \
                and q[-3] not in '()':
            a = int(q.pop())
            op = q.pop()
            b = int(q.pop())
            q.append(str(a * b))
        v = int(q.pop())
        total_sum += v
print('second answer:', total_sum)

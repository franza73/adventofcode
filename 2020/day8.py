#!/usr/local/bin/python3


def execute(P):
    ln = 0
    S = set()
    acc = 0
    while ln in P:
        cmd, val = P[ln].split()
        if cmd == 'nop':
            ln += 1
        elif cmd == 'acc':
            ln += 1
            acc += int(val)
        elif cmd == 'jmp':
            ln += int(val)
        if ln in S:
            return 'CYCLE', acc
        S.add(ln)
    return 'TERMINATE', acc


if __name__ == "__main__":

    # -- read input --
    H = {}
    line_number = 0
    with open('day8b.txt', 'r', encoding='ascii') as f:
        while True:
            line = f.readline()
            if not line:
                break
            s = line.strip()
            H[line_number] = s
            line_number += 1

    print('First question:', execute(H)[1])

    for k in sorted(H.keys()):
        if 'nop' in H[k]:
            P = dict(H)
            P[k] = H[k].replace('nop', 'jmp')
        elif 'jmp' in H[k]:
            P = dict(H)
            P[k] = H[k].replace('jmp', 'nop')
        else:
            continue
        res, acc = execute(P)
        if res == 'TERMINATE':
            print('Second question:', acc)

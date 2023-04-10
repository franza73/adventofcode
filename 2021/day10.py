#!/usr/local/bin/python3
'''
Solution to day 10 of advent of code
'''


def main():
    '''
    Processes the data while reading the input
    '''
    UP = set(list('<{[('))
    down = {'<': '>', '{': '}', '[': ']', '(': ')'}
    points = {'>': 25137, '}': 1197, ']': 57, ')': 3}
    score = {'>': 4, '}': 3, ']': 2, ')': 1}
    list_of_scores = []
    pts = 0
    with open('day10.txt', 'r', encoding='ascii') as f_d:
        while True:
            line = f_d.readline()
            if not line:
                break
            line = line.strip()
            stack = []
            is_invalid = False
            for l_i in list(line):
                if l_i in UP:
                    stack.append(l_i)
                elif stack[-1] in UP and l_i == down[stack[-1]]:
                    stack.pop()
                else:
                    pts += points[l_i]
                    is_invalid = True
                    break
            if not is_invalid:
                cnt_2 = 0
                while stack:
                    s_i = stack.pop()
                    cnt_2 = cnt_2 * 5 + score[down[s_i]]
                list_of_scores += [cnt_2]
    list_of_scores.sort()
    cnt_2 = list_of_scores[len(list_of_scores)//2]
    return pts, cnt_2


if __name__ == "__main__":
    s_1, s_2 = main()
    print('First solution:', s_1)
    print('Second solution:', s_2)

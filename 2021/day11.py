
#!/usr/local/bin/python3
'''
Advent of code day 11
'''


if __name__ == "__main__":
    M = []
    with open('day11a.txt', 'r', encoding='ascii') as f:
        while True:
            line = f.readline()
            if not line:
                break
            M += [list(map(int, list(line.strip())))]

    X, Y = len(M), len(M[0])

    # Initialize the M matrix
    N = [[0] * Y for j in range(X)]
    print(N)

# python3

import math

def solve(x, y):
    z = x/y
    print(int(math.ceil(z)))


if __name__ == '__main__':
    x, y = map(int, input().split())
    solve(x, y)

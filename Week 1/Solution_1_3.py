# python3

def solve(x):
    if x.count('9') == len(x):
        return len(x) + 1
    return len(x)


if __name__ == '__main__':
    x = input()
    print(solve(x))

# python3

def solve(X):
    res = 0
    si = 0
    sf = 0
    for x in X:
        si += x
        sf += 1/x
    res = si + round(sf, 10)
    print("%.10f" % res)


if __name__ == '__main__':
    n = int(input())
    X = [int(x) for x in input().split()]
    solve(X)

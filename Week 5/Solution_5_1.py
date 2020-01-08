# python3

def solve(A):
    tails = [0] * len(A)
    size = 0
    for x in A:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    print(size)


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    solve(A)

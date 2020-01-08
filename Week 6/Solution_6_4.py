# python3

def solve(A, k):
    res = 0
    n = len(A)
    sums = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + A[i-1][j-1]
    for i in range(k, n+1):
        for j in range(k, n+1):
            row1, col1 = i-k+1, j-k+1
            row2, col2 = i, j
            res = max(res, sums[row2][col2]-sums[row1-1][col2]-sums[row2][col1-1]+sums[row1-1][col1-1])
    print(res)


if __name__ == '__main__':
    n, k = map(int, input().split())
    A = []
    for _ in range(n):
        l = [int(i) for i in input().split()]
        A.append(l)
    solve(A, k)

# python3

def solve(A, B):
    n = len(A)
    dp = [[0]*(n+1) for _ in range(n+1)]
    res1 = []
    res2 = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = n, n
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            res1.append(i-1)
            res2.append(j-1)
            i, j = i-1, j-1
        elif dp[i][j] == dp[i-1][j]:
            i = i-1
        elif dp[i][j] == dp[i][j-1]:
            j = j-1
    print(dp[n][n])
    print(' '.join([str(e) for e in res1[::-1]]))
    print(' '.join([str(e) for e in res2[::-1]]))


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(A, B)

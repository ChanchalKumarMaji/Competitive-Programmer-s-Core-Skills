# python3

def solve(M):
    n = len(M)
    dp = [[0]*n for _ in range(n)]
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            dp[i][j] = 2**32
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + M[i-1]*M[k]*M[j]
                dp[i][j] = min(dp[i][j], q)
    return dp[1][n-1]


if __name__ == '__main__':
    n = int(input())
    M = [int(i) for i in input().split()]
    print(solve(M))

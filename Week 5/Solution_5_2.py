# python3

def solve(u, w, I, D, S):
    n, m = len(u), len(w)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + D
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + I
    for i in range(1, n+1):
        for j in range(1, m+1):
            diff = 0 if u[i-1] == w[j-1] else S
            dp[i][j] = min(dp[i][j-1]+I, dp[i-1][j-1]+diff, dp[i-1][j]+D)
    #print(dp)
    print(dp[n][m])


if __name__ == '__main__':
    n, m = map(int, input().split())
    u = input()
    w = input()
    I, D, S = map(int, input().split())
    solve(u, w, I, D, S)

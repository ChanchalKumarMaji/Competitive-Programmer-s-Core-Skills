# python3

def solve(W, weight, value):
    res = []
    n = len(weight)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w, v = weight[i-1], value[i-1]
        for j in range(W+1):
            if w > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    #print(dp)
    i, j = n, W
    while i > 0 and j > 0:
        w, v = weight[i-1], value[i-1]
        if dp[i][j] == dp[i-1][j]:
            i = i-1
        elif dp[i][j] == dp[i-1][j-w] + v:
            res.append(i)
            i, j = i-1, j-w
    print(len(res))
    print(' '.join([str(e) for e in res[::-1]]))


if __name__ == '__main__':
    n, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    solve(W, weight, value)

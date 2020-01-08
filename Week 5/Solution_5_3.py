# python3

dp = [[-1]*(162+1) for _ in range(18+1)]

def f(L, S):
    if S < 0:
        return 0
    if L == 0:
        return S == 0
    if dp[L][S] != -1:
        return dp[L][S]
    res = 0
    for k in range(10):
        res += f(L-1, S-k)
    dp[L][S] = res
    return res

def solve(L, S):
    if S == 0 and L == 1:
        return 1
    return f(L, S) - f(L-1, S)


if __name__ == '__main__':
    S, L = map(int, input().split())
    print(solve(L, S))

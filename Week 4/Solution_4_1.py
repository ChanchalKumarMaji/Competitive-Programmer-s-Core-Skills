# python3

def solve(s, Q):
    n = len(s)
    dp = [[0]*26]
    for i in range(n):
        p = dp[-1][:]
        p[ord(s[i])-97] += 1
        dp.append(p)
    for q in Q:
        l, r = q
        p = dp[r][:]
        for i in range(26):
            p[i] -= dp[l-1][i]
        m = max(p)
        for i in range(26):
            if p[i] == m:
                print(chr(i+97))
                break        


if __name__ == '__main__':
    s = input()
    q = int(input())
    Q = []
    for _ in range(q):
        l, r = map(int, input().split())
        Q.append([l, r])
    solve(s, Q)

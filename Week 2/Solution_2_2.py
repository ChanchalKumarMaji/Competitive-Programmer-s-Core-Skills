# python3

def solve(r, c):
    res = 0
    q_r, q_c = r // 3, c // 3
    r_r, r_c = r % 3, c % 3
    res += q_r * q_c * 8
    if r_c == 1:
        res += q_r * 2
    if r_c == 2:
        res += q_r * 5
    if r_r == 1:
        res += q_c * 2
    if r_r == 2:
        res += q_c * 5
    if r_r == 1 and r_c == 2:
        res += 1
    if r_r == 2 and r_c == 1:
        res += 1
    if r_r == 2 and r_c == 2:
        res += 3
    print(res)


if __name__ == '__main__':
    r, c = map(int, input().split())
    solve(r, c)

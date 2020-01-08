# python3

def solve(x, y, z):
    if x == y:
        if z == 0:
            return 0
        if z == x:
            return 1
        return -1
    k = x-y
    i1, i2 = -1, -1
    if 2*z % k == 0:
        p = 2*z // k
        if p % 2 == 0:
            i1 = p
    if (2*z-(x+y)) % k == 0:
        p = (2*z-(x+y)) // k
        if p % 2 == 1:
            i2 = p
    if i1 >= 1 and i2 >= 1:
        return min(i1, i2)
    elif i1 < 1 and i2 >= 1:
        return i2
    elif i2 < 1 and i1 >= 1:
        return i1
    return -1


if __name__ == '__main__':
    x, y, z = map(int, input().split())
    print(solve(x, y, z))

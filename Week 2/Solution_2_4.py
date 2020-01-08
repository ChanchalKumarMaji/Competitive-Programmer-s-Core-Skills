# python3

def solve(s):
    nums = []
    f = 1
    l = 0
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            num = int(s[l:i])*f
            l = i+1
            nums.append(num)
            if s[i] == '+':
                f = 1
            else:
                f = -1
    nums.append(int(s[l:])*f)
    return sum(nums)


if __name__ == '__main__':
    s = input()
    print(solve(s))

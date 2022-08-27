# https://www.acmicpc.net/problem/3058
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    s = 0
    mn = 10**6

    for num in nums:
        if num % 2 == 0:
            s += num
            mn = min(mn, num)

    print(s, mn)

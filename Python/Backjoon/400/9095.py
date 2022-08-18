# https://www.acmicpc.net/problem/9095
# D[n] = D[n-3] + D[n-2] + D[n-1]
for i in range(int(input())):
    n = int(input())
    dp = [1, 1, 2]

    for i in range(3, n + 1):
        dp.append(dp[-1] + dp[-2] + dp[-3])

    print(dp[n])

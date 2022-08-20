# https://www.acmicpc.net/problem/9095
# n = n-1 + 1
# n = n-2 + 2
# n = n-3 + 3
# D[n] = D[n-1] + D[n-2] + D[n-3]
for i in range(int(input())):
    n = int(input())
    # dp[0] 의 경우 수를 아무것도 사용하지 않는 경우의 수를 1로 포함
    dp = [1, 1, 2]

    for i in range(3, n + 1):
        dp.append(dp[-1] + dp[-2] + dp[-3])

    print(dp[n])

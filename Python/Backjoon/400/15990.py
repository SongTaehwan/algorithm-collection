# https://www.acmicpc.net/problem/15990
# n = 2 또는 3을 더한 수 + 1
# n = 1 또는 3을 더한 수 + 2
# n = 1 또는 2을 더한 수 + 3
# D[i][1] = D[n-1][2] + D[n-1][3]
# D[i][2] = D[n-2][1] + D[n-2][3]
# D[i][3] = D[n-3][1] + D[n-3][2]
import sys

limit = 10 ** 5
m = 10 ** 9 + 9

dp = [[0] * 4 for _ in range(limit + 1)]

for i in range(1, limit + 1):
    if i > 1:
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % m
    elif i == 1:
        dp[i][1] = 1
    elif i < 1:
        dp[i][1] = 0

    if i > 2:
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % m
    elif i == 2:
        dp[i][2] = 1
    elif i < 2:
        dp[i][2] = 0

    if i > 3:
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % m
    elif i == 3:
        dp[i][3] = 1
    elif i < 3:
        dp[i][3] = 0

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % m)

# Refactor

limit = 10 ** 5
m = 10 ** 9 + 9

dp = [[0] * 4 for _ in range(limit + 1)]
dp[1] = [0, 1, 0, 0]  # 1 만드는 방법 = 1
dp[2] = [0, 0, 1, 0]  # 2 만드는 방법 = 2
dp[3] = [0, 1, 1, 1]  # 3 만드는 방법 = 2+1, 1+2, 3

for i in range(4, limit + 1):
    # 마지막으로 더한 수가 1이면 직전수는 2 또는 3을 더한 수
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % m
    # 마지막으로 더한 수가 2이면 직전수는 1 또는 3을 더한 수
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % m
    # 마지막으로 더한 수가 3이면 직전수는 1 또는 2을 더한 수
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % m

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % m)

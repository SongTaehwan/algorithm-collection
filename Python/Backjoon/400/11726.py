# https://www.acmicpc.net/problem/11726
# https://www.notion.so/songtaehwan/6-c4caa5612f0b49b783fe1b41e67da825#cd68c5b2e43d4aa493834cb4f6053e8c
n = int(input())
dp = [0] * 1001  # 2*0, 2*1, 2*2
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 10007

print(dp[n])

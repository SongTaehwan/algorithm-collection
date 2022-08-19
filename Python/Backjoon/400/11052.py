# https://www.acmicpc.net/problem/11052
N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for n in range(1, N+1):  # N 만큼 순회
    for i in range(1, n + 1):
        dp[n] = max(dp[n], dp[n-i] + p[i])

print(dp[n])

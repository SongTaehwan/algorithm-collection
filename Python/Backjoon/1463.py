# https://www.acmicpc.net/problem/1463
# 8 -> 4 -> 2 -> 1
# 9 -> 3 -> 1
# 그리디로 풀 수  없다. 반례는 10
# 10 -> 5 -> 4 -> 2 -> 1 4번
# 10 -> 9 -> 3 -> 1 3번
# Top-down
import sys

sys.setrecursionlimit(10**6)
n = int(input())
dp = {1: 0}


def go(n: int) -> int:
    if n in dp:  # 캐시 데이터
        return dp[n]

    dp[n] = go(n-1) + 1

    if n % 3 == 0:
        temp = go(n//3) + 1

        if dp[n] > temp:
            dp[n] = temp

    if n % 2 == 0:
        temp = go(n//2) + 1

        if dp[n] > temp:
            dp[n] = temp

    return dp[n]


print(go(n))

# Bottom-up
n = int(input())
dp = [0, 0]

for i in range(2, n+1):
    dp.append(dp[i-1] + 1)

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

print(dp[n])

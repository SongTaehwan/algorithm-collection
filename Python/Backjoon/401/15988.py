# n = n-1 + 1
# n = n-2 + 2
# n = n-3 + 3
# D[n] = D[n-1] + D[n-2] + D[n-3]
# 9095 문제에 메모이제이션 적용하는 문제
import sys

m = 10 ** 9 + 9
dp = [1, 1, 2] + [0] * (10 ** 6 - 2)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if dp[n] > 0:
        print(dp[n])
        continue

    for i in range(3, 10**6+1):
        dp[i] = ((dp[i-1] % m) + (dp[i-2] % m) + (dp[i-3] % m)) % m

    print(dp[n])

# Refactor

m = 10 ** 9 + 9
dp = [1, 1, 2]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if n < len(dp):
        print(dp[n])
        continue

    # 메모이제이션된 수 보다 n 이 크면 이어서 나머지 값 계산
    for i in range(len(dp), n + 1):
        value = ((dp[-1] % m) + (dp[-2] % m) + (dp[-3] % m)) % m
        dp.append(value)

    print(dp[n])

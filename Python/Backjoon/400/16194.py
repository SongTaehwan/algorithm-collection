# https://www.acmicpc.net/problem/16194
# https://www.notion.so/songtaehwan/7-6fbea56dfd0c49bba62d630910bed4e1#6266da3a4f7649faa62e3b2fe37ff88a
# 초기값을 -1 로 설정하는 경우
N = int(input())
p = [0] + list(map(int, input().split()))
dp = [-1] * (N+1)
dp[0] = 0  # dp[0] + p[1] 계산 시 dp[0] 값이 0 이어야함

for n in range(1, N+1):
    for i in range(1, n+1):
        if dp[n] == -1 or dp[n] > dp[n-i] + p[i]:
            # min 을 사용하면 항상 -1 이 들어가기 때문에 조건식이 필요함
            dp[n] = dp[n-i] + p[i]

print(dp[N])

# 초기값을 문제의 제한을 통해 설정하는 경우
N = int(input())
p = [0] + list(map(int, input().split()))
dp = [1000*10000] * (N+1)
dp[0] = 0  # dp[0] + p[1] 계산 시 dp[0] 값이 0 이어야함

for n in range(1, N+1):
    for i in range(1, n+1):
        dp[n] = min(dp[n], dp[n-i] + p[i])

print(dp[N])

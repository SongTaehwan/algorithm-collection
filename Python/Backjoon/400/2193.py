# https://www.acmicpc.net/problem/2193
# D[N][L] = N 자리 이친수, 마지막 수는 L
# 2차원 다이나믹
n = int(input())
d = [[0 for _ in range(2)] for _ in range(n+1)]

d[1][0] = 0
d[1][1] = 1  # 이친수 개수

for i in range(2, n+1):
    # L = 0 이면, 직전 수는 0,1 가능
    d[i][0] = d[i-1][0] + d[i-1][1]
    # L = 1 이면, 직전 수는 0만 가능
    d[i][1] = d[i-1][0]

# 마지막 수 L 이 0,1 인 경우를 모두 더하면 이친수의 개수가 된다.
print(sum(d[n]))

# 1차원 다이나믹
# D[N] = D[N-2] + D[N]
n = int(input())
d = [0 for _ in range(n+1)]
d[1] = 1

for i in range(2, n+1):
    # D[N] = 마지막 수 0 인 경우와 마지막 수가 1인 경우의 이친수의 개수
    # D[N-1] + 0 => N-1 은 0 or 1
    # => D[N-1] + 0 = 이친수
    # D[N-2] + D[N-1] + 1 => N-1 은 항상 0, N-2 는 0 or 1
    # => D[N-2] + 01 = 이친수
    d[i] = d[i-1] + d[i-2]

print(d[n])

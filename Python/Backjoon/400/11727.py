# https://www.acmicpc.net/problem/11727
# 11726 문제처럼 D[n-2] 를 한번 더 더해주면 됌
n = int(input())

tile = [0, 1, 3] + [0] * (n-2)  # 2x0, 2x1, 2x2

for i in range(3, n+1):
    tile[i] = 2 * tile[i - 2] + tile[i - 1]
    tile[i] = tile[i] % 10007

print(tile[n])

# https://www.acmicpc.net/problem/2576
result = []

for _ in range(7):
    n = int(input())

    if n % 2 == 1:
        result.append(n)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))

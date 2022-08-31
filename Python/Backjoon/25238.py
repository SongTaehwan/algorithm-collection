# https://www.acmicpc.net/problem/25238
a, b = map(int, input().split())

defense = a - a * (b / 100)

if defense >= 100:
    print(0)
else:
    print(1)

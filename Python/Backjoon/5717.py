# https://www.acmicpc.net/problem/5717
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    print(a + b)

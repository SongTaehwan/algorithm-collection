# https://www.acmicpc.net/problem/4101

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    print("No" if a <= b else "Yes")

# https://www.acmicpc.net/problem/25625
x, y = map(int, input().split())

if y > x:
    print(y-x)
else:
    print(x+y)

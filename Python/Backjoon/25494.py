# https://www.acmicpc.net/problem/25494
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))

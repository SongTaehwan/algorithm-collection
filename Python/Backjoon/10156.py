# https://www.acmicpc.net/problem/10156
a, b, c = map(int, input().split())
print(max(a * b - c, 0))

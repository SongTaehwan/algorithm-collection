# https://www.acmicpc.net/problem/288
h, m = map(int, input().split())

m = (15 + m) % 60

if m >= 15:
    h -= 1

if h < 0:
    h = 23

print(h, m)

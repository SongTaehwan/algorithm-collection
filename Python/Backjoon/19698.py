# https://www.acmicpc.net/problem/19698
n, w, h, l = map(int, input().split())
a = (w // l) * (h // l)

if n < a:
    print(n)
else:
    print(a)

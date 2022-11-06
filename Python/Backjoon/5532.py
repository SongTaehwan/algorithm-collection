# https://www.acmicpc.net/problem/5532
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

r = (a // c) + 1 if a % c > 0 else a // c
g = (b // d) + 1 if b % d > 0 else b // d

print(l - max(r, g))

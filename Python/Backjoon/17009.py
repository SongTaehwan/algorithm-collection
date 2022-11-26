# https://www.acmicpc.net/problem/17009
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

r = a * 3 + b * 2 + c
g = d * 3 + e * 2 + f

if r > g:
    print("A")
elif r == g:
    print("T")
else:
    print("B")

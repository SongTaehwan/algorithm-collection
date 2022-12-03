# https://www.acmicpc.net/problem/14489
a, b = map(int, input().split())
p = int(input()) * 2
s = a + b

if s >= p:
    print(s-p)
else:
    print(s)

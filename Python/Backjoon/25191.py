# https://www.acmicpc.net/problem/25191
a = int(input())
b, c = map(int, input().split())
if b//2+c > a:
    print(a)
else:
    print(b//2+c)

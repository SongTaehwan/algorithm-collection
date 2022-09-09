# https://www.acmicpc.net/problem/1920
input()
a = list(map(int, input().split()))
c = {}

for i in a:
    c[i] = 1

input()
m = list(map(int, input().split()))

for i in m:
    if i in c:
        print(1)
    else:
        print(0)

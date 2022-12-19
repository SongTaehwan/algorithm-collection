# https://www.acmicpc.net/problem/13118
li = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in li:
    print(li.index(x) + 1)
else:
    print(0)

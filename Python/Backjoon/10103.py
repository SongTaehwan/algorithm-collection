# https://www.acmicpc.net/problem/10103
a = 100
b = 100

for i in range(1, int(input()) + 1):
    c, d = map(int, input().split())

    if c == d:
        continue

    if c > d:
        b -= c
    else:
        a -= d

print(a)
print(b)

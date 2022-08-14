# https://www.acmicpc.net/problem/4150

a, b = 1, 1

for _ in range(int(input()) - 1):
    a, b = b, a+b

print(a)

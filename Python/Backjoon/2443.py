# https://www.acmicpc.net/problem/2443
num = int(input())
for i in range(num):
    print(" " * i + "*" * (2 * num - 1 - i * 2))

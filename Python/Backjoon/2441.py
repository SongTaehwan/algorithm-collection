# https://www.acmicpc.net/problem/2441
num = int(input())
for i in range(num):
    print(" " * i + "*" * (num - i))

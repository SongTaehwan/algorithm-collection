# https://www.acmicpc.net/problem/2439
num = int(input())

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)

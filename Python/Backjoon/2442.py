# https://www.acmicpc.net/problem/2442
num = int(input())
mx = 2 * num - 1
space = (mx - 1) // 2

for i in range(num):
    print(" " * space + "*" * (2 * i + 1))

    space -= 1

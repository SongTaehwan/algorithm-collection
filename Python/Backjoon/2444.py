# https://www.acmicpc.net/problem/2444
num = int(input())

for i in range(2 * num):
    if i < num:
        print(" " * (num - i - 1) + "*" * (2 * i + 1))
    elif i > num:
        print(" " * (i - num) + "*" * (4 * num - 1 - i * 2))

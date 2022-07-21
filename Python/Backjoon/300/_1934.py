# https://www.acmicpc.net/problem/1934
import sys

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())

    num = 0

    while True:
        num += max(a, b)

        if num % min(a, b) == 0:
            print(num)
            break

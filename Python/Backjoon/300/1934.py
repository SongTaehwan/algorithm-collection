# https://www.acmicpc.net/problem/1934

# Brute Force
import sys

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())

    num = 0

    while True:
        num += max(a, b)

        if num % min(a, b) == 0:
            print(num)
            break

# 유클리드 호제법


def gcd(a: int, b: int):

    while b > 0:
        r = a % b
        a = b
        b = r

    return a


for _ in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(int(a * b / g))

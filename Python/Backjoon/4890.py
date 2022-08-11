# https://www.acmicpc.net/problem/4890
import sys

sys.setrecursionlimit(10**6)


# 메모리 초과로 재귀 사용시 메모리 초과 에러
def gcd(a, b):
    if a == b:
        return a
    else:
        return gcd(max(a, b) - min(a, b), min(a, b))


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


while True:
    a, b = map(int, input().split())

    if not a and not b:
        break

    g = gcd(a, b)
    l = a * b // g
    print(l // g)

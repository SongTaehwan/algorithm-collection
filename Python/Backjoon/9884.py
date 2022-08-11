# https://www.acmicpc.net/problem/9884
import sys

# 파이썬 재귀 깊이 제한으로 런타임 에러 발생하기 때문에
# 아래 코드로 재귀 깊이 제한 설정을 바꿀 수 있다.
# BOJ 서버의 default 값은 1000 으로 제한되어 있음
sys.setrecursionlimit(10**6)


def gcd(a, b):
    if a == b:
        return a
    else:
        return gcd(max(a, b) - min(a, b), min(a, b))


a, b = map(int, input().split())

print(gcd(a, b))

# Refactor with loop


def gcd(a, b):
    while a != b:
        a1 = max(a, b) - min(a, b)
        b2 = min(a, b)
        a = a1
        b = b2

    return a


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())


print(gcd(a, b))

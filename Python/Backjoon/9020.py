# https://www.acmicpc.net/problem/9020
import sys

check = set(range(2, 10001))

for i in range(2, 10001):
    if i in check:
        check -= set(range(i * i, 10001, i))

for _ in range(int(sys.stdin.readline())):
    result = []
    mn = 10001
    n = int(sys.stdin.readline())

    for i in check:
        if n - i in check:
            diff = abs(i - (n - i))

            if diff < mn:
                mn = diff
                result = [i, n - i]

    print(*result)

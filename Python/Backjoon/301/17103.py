# https://www.acmicpc.net/problem/17103
import sys

check = set(range(2, 1000001))

for i in range(2, 1000001):
    if i in check:
        check -= set(range(i * i, 1000001, i))

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    result = 0

    box = check.copy()

    for i in check:
        if num - i in box:
            result += 1

            box.remove(i)

            if i != num-i:
                box.remove(num-i)

    print(result)

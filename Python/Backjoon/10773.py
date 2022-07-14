# https://www.acmicpc.net/problem/10773
import sys

s = list()

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        s.pop()
    else:
        s.append(num)

print(sum(s))

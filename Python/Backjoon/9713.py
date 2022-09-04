# https://www.acmicpc.net/problem/9713
import sys

s = 0

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    s = 0

    for i in range(1, n+1, 2):
        s += i

    print(s)

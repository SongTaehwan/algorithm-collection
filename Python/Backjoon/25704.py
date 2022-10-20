# https://www.acmicpc.net/problem/25704
import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

d = 0

if n >= 5:
    d = max(d, 500)

if n >= 10:
    d = max(d, p * 0.1)

if n >= 15:
    d = max(d, 2000)

if n >= 20:
    d = max(d, p * 0.25)

print(max(int(p - d), 0))

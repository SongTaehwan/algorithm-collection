# https://www.acmicpc.net/problem/1026
import sys

count = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
s = 0

for i in a:
    mx = max(b)
    s += mx * i
    b.remove(mx)

print(s)

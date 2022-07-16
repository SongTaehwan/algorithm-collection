# https://www.acmicpc.net/problem/2562
import sys

max = 0
position = 1

for i in range(1, 10):
    num = int(sys.stdin.readline())

    if num > max:
        max = num
        position = i

print(max)
print(position)

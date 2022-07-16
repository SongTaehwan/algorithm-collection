# https://www.acmicpc.net/problem/10818
import sys

count = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

print(array[0], array[-1])

# Refactor
count = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

mn = sys.maxsize
mx = -mn - 1

for i in array:
    if i > mx:
        mx = i
    if i < mn:
        mn = i

print(mn, mx)

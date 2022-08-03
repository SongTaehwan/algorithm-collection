# https://www.acmicpc.net/problem/5597
import sys

nums = list(range(1, 31))

for _ in range(0, 28):
    nums.remove(int(sys.stdin.readline()))

print(*nums, sep="\n")

# https://www.acmicpc.net/problem/4344
import sys

for i in range(int(input())):
    count, *nums = map(int, sys.stdin.readline().split())

    mid = sum(nums) / len(nums)
    student = 0

    for i in nums:
        if i > mid:
            student += 1

    print(f'{student / count * 100:.3f}%')

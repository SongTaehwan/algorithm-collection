# https://www.acmicpc.net/problem/10797
n = int(input())
nums = list(map(int, input().split()))

count = 0

for num in nums:
    if num == n:
        count += 1

print(count)

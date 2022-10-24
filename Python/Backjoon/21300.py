# https://www.acmicpc.net/problem/21300
nums = list(map(int, input().split()))

count = 0

for num in nums:
    count += num * 5

print(count)

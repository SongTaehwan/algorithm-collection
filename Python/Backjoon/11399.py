# https://www.acmicpc.net/problem/11399
count = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0
ac = 0

for i in nums:
    ac += i
    result += ac

print(result)

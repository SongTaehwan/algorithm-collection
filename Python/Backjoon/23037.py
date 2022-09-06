# https://www.acmicpc.net/problem/23037
nums = list(input())

result = 0

for num in nums:
    result += int(num) ** 5

print(result)

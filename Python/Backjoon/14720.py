# https://www.acmicpc.net/problem/14720
n = int(input())
nums = list(map(int, input().split()))
result = 0
milk = 0

for i in nums:
    if i == milk:
        result += 1

        milk += 1
        milk = milk % 3

print(result)

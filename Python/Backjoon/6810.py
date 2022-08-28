# https://www.acmicpc.net/problem/6810
nums = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
multiplier = 3
result = 0

while nums:
    if multiplier == 3:
        result += (nums.pop() * multiplier)
        multiplier = 1
    else:
        result += (nums.pop() * multiplier)
        multiplier = 3

result += int(input()) * 1
result += int(input()) * 3
result += int(input()) * 1

print(f"The 1-3-sum is {result}")

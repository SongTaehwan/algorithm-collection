# https://www.acmicpc.net/problem/17298
import sys
input()

lst = list(map(int, input().split()))

result = []
prev = 0

for i in range(0, len(lst) - 1):  # Brute force - worst case O(n^2)
    target = lst[i]
    subLst = lst[i + 1:]

    if prev > target:
        result.append(prev)
        continue

    if target > max(subLst):
        result.append(-1)
        continue

    for num in subLst:
        if num > target:
            result.append(num)
            prev = num
            break

result.append(-1)

print(*result)

# Refactor

count = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

result = [-1] * count
stack = [0]

for i in range(len(lst)):  # O(n)
    num = lst[i]

    if not stack:
        stack.append(i)
        continue

    while stack and lst[stack[-1]] < num:
        j = stack.pop()
        result[j] = num

    stack.append(i)

print(*result)

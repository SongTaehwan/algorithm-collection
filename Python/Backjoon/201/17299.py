# https://www.acmicpc.net/problem/17299
count = int(input())
items = list(map(int, input().split()))

result = [-1] * count
stack = list()
dic = dict()

for num in items:
    dic.setdefault(num, 0)
    dic[num] += 1

for i in range(0, len(items)):
    num = items[i]

    if not stack:
        stack.append(i)
        continue

    while stack and dic.get(items[stack[-1]]) < dic.get(items[i]):
        index = stack.pop()
        result[index] = items[i]

    stack.append(i)

print(*result)

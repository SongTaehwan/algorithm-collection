# https://www.acmicpc.net/problem/11047
count, k = map(int, input().split())
stack = []

for i in range(count):
    stack.append(int(input()))

result = 0

while k > 0:
    i = stack.pop()

    if i > k:
        continue

    result += k // i
    k %= i

print(result)

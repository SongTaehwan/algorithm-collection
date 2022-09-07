# https://www.acmicpc.net/problem/7567
plates = list(input())
stack = []
result = 10

while plates:
    stack.append(plates.pop())


while stack:
    plate = stack.pop()

    if not stack:
        break

    top = stack[len(stack)-1]

    if plate != top:
        result += 10
    else:
        result += 5

print(result)

# Refactor
plates = list(input())
result = 0

for i in range(len(plates)):
    if i == 0:
        result += 10
    elif plates[i] == plates[i-1]:
        result += 5
    else:
        result += 10

print(result)

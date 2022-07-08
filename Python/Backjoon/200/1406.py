# https://www.acmicpc.net/problem/1406
import sys

text = input()
count = int(input())

left = list()
right = list()

for char in text:
    left.append(char)

for i in range(count):
    command, *value = sys.stdin.readline().split()
    value = None if not value else value[-1]

    if command.upper() == "L":
        if left:
            right.append(left.pop())
    elif command.upper() == "D":
        if right:
            left.append(right.pop())
    elif command.upper() == "B":
        if left:
            left.pop()
    else:
        left.append(value)

while right:
    left.append(right.pop())

print("".join(left))

# https://www.acmicpc.net/problem/1316
import sys

count = int(input())
stack = list()
result = 0

for _ in range(count):
    string = sys.stdin.readline().rstrip()

    for i in string:
        if not stack:
            stack.append(i)
            continue

        top = stack[-1]

        if top == i:
            stack.append(i)
        elif i in stack:
            break
        else:
            stack.append(i)

    if len(stack) == len(string):
        result += 1

    stack = []

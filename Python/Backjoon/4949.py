# https://www.acmicpc.net/problem/4949
import sys

while True:
    stack = list()
    string = sys.stdin.readline().rstrip()

    if string == ".":
        break

    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif i == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
        elif i == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")

# Refactor
while True:
    stack = []
    string = sys.stdin.readline().rstrip()

    if string == ".":
        break

    for i in string:
        if i in "([":
            stack.append(i)
        elif i in ")]":
            if not stack:
                print("no")
                break
            elif i == ")" and stack.pop() != "(":
                print("no")
                break
            elif i == "]" and stack.pop() != "[":
                print("no")
                break
        elif i == ".":
            if stack:
                print("no")
            else:
                print("yes")

# https://www.acmicpc.net/problem/9093
import sys

count = int(input())

# for i in range(count):
#     data = " " + input()
#     stack = list()
#     word = ""

#     for i in range(0, len(data)):
#         index = -i - 1
#         char = data[index]

#         if char == " ":
#             stack.append(word)
#             word = ""
#         else:
#             word += char

#     result = ""

#     while stack:
#         result += stack.pop()

#         if len(stack) > 0:
#             result += " "

#     print(result)

# Refactor

for i in range(count):
    stack = list()

    for char in sys.stdin.readline():
        stack.append(char)

    value = ""

    while stack:
        value += stack.pop()

    stack = value.split()
    result = ""

    while stack:
        result += stack.pop()

        if len(stack) > 0:
            result += " "

    print(result)

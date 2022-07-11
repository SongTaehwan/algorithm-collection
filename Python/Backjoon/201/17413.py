# https://www.acmicpc.net/problem/17413
# 실패의 흔적
# from collections import deque
# import sys

# input = deque(sys.stdin.readline().rstrip())
# words = list()
# word = ""
# tag = ""
# count = 0

# while input:
#     char = input.popleft()

#     if char == "<":
#         count += 1
#         tag += char

#         if word:
#             words.append(word)
#             word = ""

#     elif char == ">":
#         count -= 1
#         tag += char

#         words.append(tag)

#         tag = ""

#     elif count > 0:
#         tag += char
#     else:
#         word += char

# if len(input) == 0 and word:
#     words.append(word)
#     word = ""


# print(words)
# result = ""

# for word in words:
#     if word[0] == "<":
#         result += word
#     else:
#         stack = word.split()
#         stack.reverse()
#         stack = list(" ".join(stack))

#         while len(stack) != 0:
#             result += stack.pop()

# print(result)

# 접근법은 맞았음
# 태그의 안인지 밖인지 구분해서 뒤집을지 말지 결정해야 한다.
import sys

input = list(sys.stdin.readline().rstrip())
tag = False
stack = list()
result = ""

for char in input:
    if char == "<":
        while len(stack) != 0:
            result += stack.pop()
        tag = True
        result += char
    elif char == ">":
        tag = False
        result += char
    elif tag == True:
        result += char
    else:
        if char == " ":
            while len(stack) != 0:
                result += stack.pop()
            result += " "
        else:
            stack.append(char)

while len(stack) != 0:
    result += stack.pop()

print(result.rstrip())

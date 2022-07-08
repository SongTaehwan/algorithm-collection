# https://www.acmicpc.net/problem/9012
import sys

# for i in range(int(input())):
#     ps = sys.stdin.readline()
#     open = 0

#     for char in ps:
#         if char == "(":
#             open += 1
#         elif char == ")":
#             open -= 1

#         if open < 0:
#             break

#     if open != 0:
#         print("NO")
#     else:
#         print("YES")

# Stack 사용한 풀이


def valid(ps):
    stack = list()

    for char in ps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "NO"

            stack.pop()

    if stack:
        return "NO"
    else:
        return "YES"


for i in range(int(input())):
    print(valid(sys.stdin.readline()))

# https://www.acmicpc.net/problem/9012
import sys

for i in range(int(input())):
    ps = sys.stdin.readline()
    open = 0

    for char in ps:
        if char == "(":
            open += 1
        elif char == ")":
            open -= 1

        if open < 0:
            break

    if open != 0:
        print("NO")
    else:
        print("YES")

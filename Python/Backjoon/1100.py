# https://www.acmicpc.net/problem/1100
import sys

result = 0

for i in range(8):
    row = list(sys.stdin.readline())

    for j in range(8):
        if (i + j) % 2 == 0 and row[j] == "F":
            result += 1

print(result)

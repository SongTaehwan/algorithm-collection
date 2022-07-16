# https://www.acmicpc.net/problem/3052
import sys

result = set()

for i in range(10):
    num = int(sys.stdin.readline())
    result.add(num % 42)

print(len(result))

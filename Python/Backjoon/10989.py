# https://www.acmicpc.net/problem/10989
# counting sort implementation
import sys

n = int(input())
result = [0] * 10001

for _ in range(n):
    result[int(sys.stdin.readline())] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i)

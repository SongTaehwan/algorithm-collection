# https://www.acmicpc.net/problem/2738
import sys

n, m = map(int, input().split())

a = []
b = []

for _ in range(n * 2):
    row = list(map(int, sys.stdin.readline().split()))

    if len(a) != n:
        a.append(row)
    else:
        b.append(row)

for i in range(0, n):
    rowA = a[i]
    rowB = b[i]

    rowSum = []

    for j in range(0, m):
        rowSum.append(rowA[j] + rowB[j])

    print(*rowSum)

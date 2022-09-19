# https://www.acmicpc.net/problem/23968
import sys


n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(n):
    swapped = False

    for j in range(n - i - 1):
        if s[j] > s[j + 1]:
            s[j], s[j+1] = s[j+1], s[j]
            count += 1
            swapped = True

        if count == k:
            print(s[j], s[j + 1])
            exit()

    if swapped == False:
        break

print(-1)

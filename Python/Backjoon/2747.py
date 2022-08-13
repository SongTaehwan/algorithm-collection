# https://www.acmicpc.net/problem/2747
n = int(input())

memo = [0, 1, 1]

for i in range(3, n + 1):
    memo.append(memo[-1] + memo[-2])

print(memo.pop())

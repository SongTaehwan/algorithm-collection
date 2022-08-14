# https://www.acmicpc.net/problem/14495

n = int(input())
memo = [0, 1, 1, 1]

for i in range(4, n+1):
    memo.append(memo[-1] + memo[-3])

print(memo[n])

# https://www.acmicpc.net/problem/15624
# 피사노 주기로 풀이할 것
n = int(input())
m = 10 ** 9 + 7
p = 15 * (10 ** 8) + 7

a, b = 0, 1

for _ in range(n % p):
    a, b = b, (a + b) % m

print(a)

# Array
n = int(input())
m = 10 ** 9 + 7
p = 15 * (10 ** 8)

memo = [0, 1]

for _ in range(n % p):
    memo.append((memo[-1] + memo[-2]) % m)

print(memo[n])

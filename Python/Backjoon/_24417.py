# https://www.acmicpc.net/problem/24417
n = int(input())
m = 10 ** 9 + 7
p = 15 * 10 ** 8 + 7

a, b = 0, 1
for _ in range(n % p):
    a, b = b, (a+b) % m

print(a, n - 2)

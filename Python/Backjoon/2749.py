# https://www.acmicpc.net/problem/2749
m = 10 ** 6  # 10^n
p = 15 * 10 ** 5  # 15 * 10^n-1
n = int(input())
r = n % p

a, b = 0, 1

for _ in range(r):
    a, b = b, (a+b) % m
    print(a, b)

print(a)

# m = 1000000  # 10^6
# p = 15 * 10 ^ 5 = 1500000
# 나누는 수(m)가 100만이면, 주기(p)는 150만
# fibo(n) % 100만 == n%p % 100만

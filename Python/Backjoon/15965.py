# https://www.acmicpc.net/problem/15965
from math import sqrt

n = 7369000
primes = [1] * (n + 1)

for i in range(2, int(sqrt(n)) + 1):
    if primes[i] == 1:
        j = i * i

        while j <= n:
            primes[j] = 0
            j += i

primes = [i for i in range(2, n) if primes[i]]

k = int(input())
print(primes[k-1])

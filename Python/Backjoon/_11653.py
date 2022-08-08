# https://www.acmicpc.net/problem/11653
def validatePrime(v):
    if v < 2:
        return False

    i = 2

    while i * i <= num:  # 1과 자기 자신만 아니면 됌
        if v % i == 0:
            return False

        i += 1

    return True


def getPrimes(v):
    primes = set(range(2, v + 1))

    for i in range(2, v + 1):
        if i in primes:
            primes -= set(range(i * i, v + 1, i))

    return primes


primes = getPrimes(10000000)
print(primes)
num = int(input())

prime = primes[0]

while num > 1:
    if num % 2 == 0:
        num //= 2

    if validatePrime(num):
        print(num)
        break

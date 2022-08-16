# https://www.acmicpc.net/problem/11653
n = int(input())
i = 2

while n > 1:
    if n % i == 0:
        print(i)
        n //= i
    else:
        i += 1

# Refactor
n = int(input())
i = 2
r = int(n ** 0.5)  # 약수는 n 의 n^0.5 보다 작음

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1

if n > 1:
    print(n)  # 마지막 몫(소수)

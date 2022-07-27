# https://www.acmicpc.net/problem/1978
# O(N)
count = int(input())
nums = list(map(int, input().split()))

result = 0

for num in nums:
    if num <= 1:
        continue

    target = num - 1

    while target > 1:
        if num % target == 0:
            break

        target -= 1

    if target == 1:
        result += 1

print(result)

# Refactor -> O(N)
count = int(input())
nums = list(map(int, input().split()))

result = 0

for num in nums:
    if num <= 1:
        continue

    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        result += 1

print(result)

# Refactor -> O(N/2)
count = int(input())
nums = list(map(int, input().split()))

result = 0

for num in nums:
    if num <= 1:
        continue

    isPrime = True

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        result += 1

print(result)

# Refactor -> O(sqrt(N))
count = int(input())
nums = list(map(int, input().split()))

result = 0

for num in nums:
    if num <= 1:
        continue

    isPrime = True

    i = 2

    while i * i <= num:
        if num % i == 0:
            isPrime = False
            break

        i += 1

    if isPrime:
        result += 1

print(result)

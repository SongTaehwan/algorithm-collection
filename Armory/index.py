# 약수 판별 - a 가 b 의 약수인지?
import math


def validDivider(a: int, b: int):
    # a 로 나머지가 0 이면 약수
    # b 는 a 의 배수
    return b % a == 0


# 배수 판별 - a가 b의 배수인지?
def validMultiplier(a: int, b: int):
    # b 로 나눈 나머지가 0 이면 배수
    # b 는 a 의 약수
    return a % b == 0


# 모든 약수 구하기 O(N)
def findAllDivider(number: int) -> list[int]:
    result = [1]  # 1 은 모든 수의 약수

    # number 의 가장 큰 약수는 number / 2 보다 항상 작거나 같음
    # => O(N/2) == O(N)
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result.append(i)

    return result


# 참고: https://www.geeksforgeeks.org/find-all-divisors-of-a-natural-number-set-2/
# 모든 약수 구하기 O(sqrt(N))
def findAllDividerFaster(n: int) -> list[int]:
    result = []

    # List to store half of the divisors
    for i in range(1, int(math.sqrt(n) + 1)):

        if (n % i == 0):
            # 100의 경우 10 * 10 으로 동일하기 때문에 한번만 넣음
            if (n / i == i):
                result.append(i)
            else:
                result.append(i)
                result.append(n // i)

    return result  # 정렬은 되어있지 않음


# 모든 약수 구하기 O(sqrt(N)) + 정렬
def findAllDividerFasterInOrder(n: int) -> list[int]:
    i = 1
    a = []
    b = []

    # i < sqrt(n)
    # i^2 < n
    # 약수 페어 중 작은 약수 찾기
    while (i * i < n):
        if n % i == 0:
            a.append(i)
        i += 1

    # 큰 약수 찾기
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            b.append(n // i)

    return a + b


# 최대공약수 - O(N) - 브루트 포스
def gcd(a: int, b: int) -> int:
    answer = 1

    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i

    return answer


# 최대공약수 - 유클리드 호제법 - 재귀(느린 버전)
def gcd(a, b):
    while a != b:
        a1 = max(a, b) - min(a, b)
        b2 = min(a, b)
        a = a1
        b = b2

    return a


# 최대공약수 - 유클리드 호제법 - 재귀(느린 버전)
def gcd(a, b):
    if a == b:
        return a
    else:
        return gcd(max(a, b) - min(a, b), min(a, b))


# 최대공약수 - 유클리드 호제법 - 재귀 O(logN)
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 최대공약수 - 유클리드 호제법 - 반복문 O(logN)
def gcd(a: int, b: int) -> int:
    while b > 0:
        r = a % b
        a = b
        b = r

    return a


# 최소공배수
# LCM = A * B / GCD
def LCM(a: int, b: int) -> int:
    g = gcd(a, b)
    return int(a * b / g)


# 소수 찾기 - O(n)
nums = list(map(int, input().split()))  # [1,2,3,4,5,6,7...]
result = 0

for num in nums:
    if num <= 1:  # 2는 소수
        continue

    isPrime = True

    # 2~num-1
    for i in range(2, num):  # O(n)
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        result += 1

# 소수 찾기 - O(n/2)
nums = list(map(int, input().split()))
result = 0

for num in nums:
    if num <= 1:
        continue

    isPrime = True

    for i in range(2, int(num / 2) + 1):
        # 나누어 떨어진다는 것은 약수를 의미한다. num 의 약수 중에서 가장 큰 것은 num/2 보다 작거나 같다.
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        result += 1

# 소수 찾기 - O(sqrt n)
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

# 소수 찾기 - 에라토스테네스의 체 - O(nlog logn) - for loop
# 1929
a, b = map(int, input().split())
check = [False] * (b + 1)

for i in range(2, b + 1):  # O(NloglogN)
    if check[i] == False:
        if i >= a:
            print(i)

        j = i * i

        while j <= b:
            check[j] = True
            j += i

# 소수 찾기 - 에라토스테네스의 체 - Set
a, b = map(int, input().split())
check = set(range(2, b + 1))

for i in range(2, b + 1):
    if i in check:
        check -= set(range(i * i, b + 1, i))

        if i >= a:
            print(i)


# 피보나치 수 - 재귀(Top-down) - O(2^n)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        # n 을 구하려면 n-1, n-2 를 구해야함(하나 구하려면 두개를 구해야하는 구조)
        return fibonacci(n-1) + fibonacci(n-2)


# 피보나치 수 - 재귀(optimal substructure) O(n) = 문제의 개수(n) * 문제 1개를 푸는 시간(덧셈은 O(1))
memo = [0, 1] * [0] * (n - 1)


def fibonacci(n: int) -> int:
    global memo

    if n <= 1:
        return n
    else:
        if memo[n]:
            return memo[n]

        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

# 피보나치 수 - 반복문(Bottom-up)


nums = [0, 1]


def fibonacci(n: int) -> int:
    global nums

    for i in range(2, n + 1):
        nums[i] = nums[i-1] + nums[i-2]
        # nums.append(nums[i-1] + nums[i-2])

    return nums[n]


# 피보나치 수 - 반복문(Bottom-up) without memoization
def fibonacci(n: int) -> int:
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

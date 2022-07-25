# 최대공약수 - O(N)
def gcd(a: int, b: int) -> int:
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i

    return 1


# 유클리드 호제법 - 재귀 O(logN)
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 유클리드 호제법 - 반복문 O(logN)
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

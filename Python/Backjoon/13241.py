# https://www.acmicpc.net/problem/13241
def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print(a * b // gcd(a, b))

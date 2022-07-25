# https://www.acmicpc.net/problem/2609

# 유클리드 호제법
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
g = gcd(a, b)
l = a * b / g

print(g, int(l))

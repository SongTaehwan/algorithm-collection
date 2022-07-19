# https://www.acmicpc.net/problem/2908

def reverse(n: int) -> int:
    result = 0

    while n > 0:
        result *= 10
        result += n % 10
        n //= 10

    return result


a, b = map(int, input().split())

print(max(reverse(a), reverse(b)))

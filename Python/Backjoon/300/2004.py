# https://www.acmicpc.net/problem/2004
def calc(n, v) -> int:
    result = 0
    i = v

    while i <= n:
        result += n // i
        i *= v

    return result


n, m = map(int, input().split())

two = calc(n, 2)
two -= calc(n-m, 2)
two -= calc(m, 2)

five = calc(n, 5)
five -= calc(n-m, 5)
five -= calc(m, 5)

print(min(two, five))

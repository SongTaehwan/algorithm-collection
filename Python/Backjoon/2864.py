# https://www.acmicpc.net/problem/2864
# 5 -> 6, 6 -> 6 최대
# 5 -> 5, 6 -> 5 최소

def calc(n):
    mn = 0
    mx = 0
    i = 1

    while n > 0:
        m = n % 10

        if m == 5:
            mn += 5 * i
            mx += 6 * i
        elif m == 6:
            mn += 5 * i
            mx += 6 * i
        else:
            mn += m * i
            mx += m * i

        n //= 10
        i *= 10

    return [mn, mx]


a, b = map(int, input().split())

r = calc(a, 5)
r2 = calc(b, 6)

print(r[0] + r2[0], r[1] + r2[1])

# Others
a, b = input().split()

mn = int(a.replace('6', '5')) + int(b.replace('6', '5'))
mx = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(mn, mx)

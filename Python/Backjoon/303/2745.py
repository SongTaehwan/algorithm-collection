# https://www.acmicpc.net/problem/2745
# B 진법 수 N을 10진수로 바꾸려면 B^k 를 곱하면서 더해가면 된다.
# 3진법 수 102 = 1 * 3^2 + 0 * 3^1 + 2 * 3^0 = 11
n, b = input().split()
b = int(b)

result = 0

for i in range(0, len(n)):
    value = ord(n[i])

    if value >= 65:
        value = value - 55
    else:
        value = value - 48

    digit = len(n) - 1 - i
    result += value * (b ** digit)

print(result)

# https://www.acmicpc.net/problem/11005
n, b = map(int, input().split())
result = ""

while n > 0:
    m = n % b

    if m >= 10:
        result += chr(m + 55)
    else:
        result += str(m)

    n //= b

print(result[::-1])

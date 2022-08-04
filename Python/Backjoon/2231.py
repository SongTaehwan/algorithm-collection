# https://www.acmicpc.net/problem/2231
num = int(input())

i = 1
result = 0

while i <= num:
    sum = i
    a = i

    while a > 0:
        sum += a % 10
        a //= 10

    if sum == num:
        result = i
        break
    else:
        i += 1

print(result)

# https://www.acmicpc.net/problem/1676

# Brute force
count = 1
result = 0

for i in range(1, int(input()) + 1):
    count *= i

while count > 0:
    modular = count % 10

    if modular == 0:
        result += 1
        count //= 10
    else:
        break

print(result)

# 5의 개수 찾기
n = int(input())

result = 0
square = 5

while square <= n:
    result += n // square
    square *= 5

print(result)


# Refactor
def calc(n, v) -> int:
    result = 0
    i = v

    while i <= n:
        result += n // i
        i *= v

    return result


n = int(input())
print(calc(n, 5))

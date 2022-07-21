# https://www.acmicpc.net/problem/1676

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

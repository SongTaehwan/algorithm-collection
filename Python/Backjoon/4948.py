# https://www.acmicpc.net/problem/4948
n = 123456 * 2
count = 0
check = set(range(2, n + 1))

for i in range(2, n+1):
    if i in check:
        check -= set(range(i * i, n + 1, i))

while True:
    n = int(input())

    if n == 0:
        break

    for num in check:
        if num > 2*n:
            break

        if num > n and num <= 2*n:
            count += 1

    print(count)
    count = 0

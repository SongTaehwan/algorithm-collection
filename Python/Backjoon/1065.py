# https://www.acmicpc.net/problem/1065
n = int(input())

result = 0

for i in range(1, n + 1):
    if i < 100:
        result += 1
        continue

    m1 = i % 10
    j = i // 10

    m2 = j % 10
    j = j // 10

    diff = m1 - m2

    m1 = m2

    while j > 0:
        m2 = j % 10

        if diff != m1 - m2:
            break
        else:
            m1 = m2

        j //= 10

    if j == 0:
        result += 1

print(result)

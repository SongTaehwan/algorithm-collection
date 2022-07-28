# https://www.acmicpc.net/problem/1929
a, b = map(int, input().split())

check = []

for i in range(0, b + 1):
    check.append(False)

i = 2

# 에라토스테네스의 체
while i <= b:  # O(NloglogN)
    if check[i] == False:
        if i >= a:
            print(i)

        j = i * i

        while j <= b:
            check[j] = True
            j += i

    i += 1

# 에라토스테네스의 체 with Set
a, b = map(int, input().split())

check = set(range(2, b + 1))

for i in range(2, b + 1):
    if i in check:
        check -= set(range(i * i, b + 1, i))

        if i >= a:
            print(i)

# https://www.acmicpc.net/problem/1929
a, b = map(int, input().split())

check = []
result = []


for i in range(0, b + 1):
    check.append(False)

i = 2

while i <= b:  # O(NloglogN)
    if check[i] == False:
        if i >= a:
            print(i)

        j = i * i

        while j <= b:
            check[j] = True
            j += i

    i += 1

# https://www.acmicpc.net/problem/2960
n, k = map(int, input().split())

check = [False] * (n + 1)
count = 0

for i in range(2, n + 1):
    if check[i] == False:
        j = i

        while j <= n:
            if check[j] == False:
                check[j] = True
                count += 1

                if count == k:
                    print(j)
                    break

            j += i

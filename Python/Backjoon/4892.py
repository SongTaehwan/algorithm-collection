# https://www.acmicpc.net/problem/4892
i = 1

while True:
    n0 = int(input())

    if n0 == 0:
        break

    n1 = 3 * n0
    n2 = n1 // 2 if n1 % 2 == 0 else (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 / 9

    if n1 % 2 == 0:
        print(f"{i}. even {int(n4)}")
    else:
        print(f"{i}. odd {int(n4)}")

    i += 1

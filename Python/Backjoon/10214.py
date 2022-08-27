# https://www.acmicpc.net/problem/10214
for _ in range(int(input())):
    y = k = 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b

    print("Yonsei" if y > k else "Korea")

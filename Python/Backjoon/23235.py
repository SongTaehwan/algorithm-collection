# https://www.acmicpc.net/problem/23235
i = 0

while True:
    a, *v = map(int, input().split())

    if a == 0:
        break

    i += 1

    print(f"Case {i}: Sorting... done!")

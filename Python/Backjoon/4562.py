# https://www.acmicpc.net/problem/4562

for _ in range(int(input())):
    brains, requirement = map(int, input().split())

    if brains >= requirement:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")

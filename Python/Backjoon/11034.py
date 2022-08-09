# https://www.acmicpc.net/problem/11034
while True:
    try:
        a, b, c = map(int, input().split())
        count = max(b-a, c-b) - 1
        print(count)

    except:
        break

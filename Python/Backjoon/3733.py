# https://www.acmicpc.net/problem/3733

while True:
    try:
        a, b = map(int, input().split())
        print(b // (a+1))
    except:
        break

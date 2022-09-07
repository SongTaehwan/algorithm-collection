# https://www.acmicpc.net/problem/5086
while True:
    a, b = map(int, input().split())

    if not a and not b:
        break

    # a 가 b 의 약수
    if not (b % a):
        print("factor")
    # a 가 b 의 배수
    elif not (a % b):
        print("multiple")
    else:
        print("neither")

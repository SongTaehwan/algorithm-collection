# https://www.acmicpc.net/problem/9471
# 피사노 주기
# 피보나치 수와 나눗셈할 수(m)이 아주 큰 경우에 사용하기 좋은 알고리즘
# 나눈 나머지 값이 특정 주기로 반복됨을 이용하는 알고리즘
for _ in range(int(input())):
    n, m = map(int, input().split())

    a = 0
    b = 1
    result = 0

    while True:
        # 일정 주기로 나머지 값이 반복되기 때문에
        # fn-1 + fn-2 값을 m 으로 나눈 나머지 값을 주기를 모두 구할 때 까지 계산
        a, b = b, (a+b) % m
        result += 1

        # 주기의 시작인 0과 1 이 되면 주기를 모두 구한 것으로 판단
        if a == 0 and b == 1:
            break

    print(n, result)

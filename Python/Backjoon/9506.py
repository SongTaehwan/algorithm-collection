# https://www.acmicpc.net/problem/9506
while True:
    n = int(input())

    if n == -1:
        break

    s = [1]  # 1은 모든 수의 약수
    r = 0

    # n 의 가장 큰 약수는 n / 2 보다 항상 작음
    for i in range(2, n//2 + 1):
        if not n % i:
            s.append(str(i))
            r += i

    if r == n:
        print(f"{n} = {' + '.join(s)}")
    else:
        print(f"{n} is NOT perfect.")

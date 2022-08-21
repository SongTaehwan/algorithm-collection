# https://www.acmicpc.net/problem/10844
# n = l + 1 + l (직전 수가 1 큰 경우)
# n = l - 1 + l (직전 수가 1 작은 경우)
# D[n][l] = 길이가 N 인 계단 수의 총 갯수, 마지막 수 L
# D[n][l] = D[n-1][l+1] + D[n-1][l-1]
m = 10 ** 9
n = int(input())
d = [[0] * 10 for _ in range(n+1)]
d[1] = [0] + [1] * 9  # 0 으로 시작하는 수는 계단 수가 아니다.
# d[2][0] 의 반례는 10

for i in range(2, n+1):
    # 마지막 수로 사용할 수 있는 숫자는 0 부터 9 까지 10개
    for l in range(10):
        d[i][l] = 0
        # 예외 처리 l = 9
        if l > 0:  # l = 0 인 경우 패스
            # l+1 = 10 이므로 계단 수가 아니다. 따라서 l-1 경우만 더한다.
            # d[i-1][l-1] 를 더하고 다음 if 절은 생략한다.
            d[i][l] += d[i-1][l-1]

        # 예외 처리 l = 0
        if l < 9:  # l = 9 인 경우 패스
            # l-1 = -1 이므로 l+1 경우만 더한다.
            # 첫 if 절은 생략하고 d[i-1][l+1] 만 더 한다.
            d[i][l] += d[i-1][l+1]

        d[i][l] %= m

print(sum(d[n]) % m)

# Another version (Easy to understand)
m = 10 ** 9
n = int(input())
d = [[0] * 10 for _ in range(n+1)]
d[1] = [0] + [1] * 9  # 0 으로 시작하는 수는 계단 수가 아니다.
# d[2][0] 의 반례는 10

for i in range(2, n+1):
    # 마지막 수로 사용할 수 있는 숫자는 0 부터 9 까지 10개
    for l in range(10):
        # 예외 처리 l = 9
        if l == 9:  # l = 0 인 경우 패스
            # l+1 = 10 이므로 계단 수가 아니다. 따라서 l-1 경우만 더한다.
            # d[i-1][l-1] 를 더하고 다음 if 절은 생략한다.
            d[i][l] += d[i-1][l-1]

        # 예외 처리 l = 0
        elif l == 0:  # l = 9 인 경우 패스
            # l-1 = -1 이므로 l+1 경우만 더한다.
            # 첫 if 절은 생략하고 d[i-1][l+1] 만 더 한다.
            d[i][l] += d[i-1][l+1]
        else:
            d[i][l] = d[i-1][l+1] + d[i-1][l-1]

        d[i][l] %= m

print(sum(d[n]) % m)

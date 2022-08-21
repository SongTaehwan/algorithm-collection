# https://www.acmicpc.net/problem/9655
# n = n-1 + 1 마지막 남은 돌이 1 인 경우
# n = n-3 + 3 마지막 남은 돌이 3 인 경우
n = int(input())
# SK - 1, CY - 0
d = [0] * 1001
# SK 가 이기면 1, 지면 0
d[1] = 1  # 돌이 1개 또는 3개면 SK 가 이김
d[2] = 0  # 돌이 2개면 CY 가 이김
d[3] = 1

for i in range(4, n+1):
    if d[i-1] == 1 or d[i-3] == 1:
        # 돌이 2, 4개면 SK 는 1개만 가져갈 수 있고 나머지를 CY 가 가져가기 때문에 진다.
        d[i] = 0
    else:
        d[i] = 1

if d[n] == 1:
    print("SK")
else:
    print("CY")

# Another version
n = int(input())

if n % 2 != 0:
    print("SK")
else:
    print("CY")

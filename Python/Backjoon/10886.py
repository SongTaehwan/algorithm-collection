# https://www.acmicpc.net/problem/10886
n = int(input())
result = 0

for _ in range(n):
    result += int(input())

if result * 2 > n:  # 과반 이상
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

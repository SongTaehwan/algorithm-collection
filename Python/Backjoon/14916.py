# https://www.acmicpc.net/problem/14916
n = int(input())

if n % 5 % 2 == 0:
    print(n // 5 + (n % 5) // 2)
elif n > 5:
    print(-1 + n // 5 + ((n % 5) + 5) // 2)
else:
    print(-1)

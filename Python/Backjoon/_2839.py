# https://www.acmicpc.net/problem/2839
n = int(input())


if n % 5 % 3 == 0:
    print(n // 5 + (n % 5) // 3)
elif n % 5 == 0:
    print(n//5)
elif n % 3 == 0:
    print(n//3)
else:
    count = 0
    print("in")

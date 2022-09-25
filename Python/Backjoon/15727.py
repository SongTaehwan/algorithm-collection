# https://www.acmicpc.net/problem/15727
n = int(input())
print((n // 5) + (1 if n % 5 != 0 else 0))

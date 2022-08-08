# https://www.acmicpc.net/problem/25304
x = int(input())

for _ in range(int(input())):
    a, b = map(int, input().split())
    x -= a * b

print("Yes" if x == 0 else "No")

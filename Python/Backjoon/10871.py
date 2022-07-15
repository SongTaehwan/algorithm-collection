# https://www.acmicpc.net/problem/10871
n, x = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if i < x:
        print(i, end=" ")

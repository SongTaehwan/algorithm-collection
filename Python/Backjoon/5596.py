# https://www.acmicpc.net/problem/5596
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max(sum(a), sum(b)))

# https://www.acmicpc.net/problem/2525
h, m = map(int, input().split())
time = int(input())

m = h * 60 + m + time
h = m // 60 % 24
mins = m % 60

print(h, mins)

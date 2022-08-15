# https://www.acmicpc.net/problem/2530
h, m, s = map(int, input().split())
t = int(input())

s += t
m += s // 60
s = s % 60
h += m // 60
m = m % 60
h = h % 24

print(h, m, s)

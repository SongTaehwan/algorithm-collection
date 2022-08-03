# https://www.acmicpc.net/problem/1085
x, y, w, h = map(int, input().split())
print(min(w-x, h-y, x, y))

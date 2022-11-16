# https://www.acmicpc.net/problem/20499
k, d, a = map(int, input().split(sep="/"))
if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")

# https://www.acmicpc.net/problem/24736
for _ in range(2):
    t, f, s, p, c = map(int, input().split())
    print(t*6 + f*3 + s*2 + p + c*2, end=" ")

# https://www.acmicpc.net/problem/11549
t = int(input())
tmp = map(int, input().split())
ans = 0

for i in tmp:
    if i == t:
        ans += 1

print(ans)

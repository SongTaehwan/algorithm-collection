ans = 1000000

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a <= b:
        ans = min(ans, b)

if ans == 1000000:
    print(-1)
else:
    print(ans)

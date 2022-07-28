# https://www.acmicpc.net/problem/2581
a = int(input())
b = int(input())

check = set(range(2, b + 1))

for i in range(2, b + 1):
    if i in check:
        check -= set(range(i * i, b + 1, i))

        if i < a:
            check.discard(i)

if len(check):
    print(sum(check))
    print(min(check))
else:
    print(-1)

# https://www.acmicpc.net/problem/1789
s = int(input())

i = 1
count = 0

while s > 0:
    if s - i < 0:
        break

    count += 1
    s -= i
    i += 1

print(count)

# https://www.acmicpc.net/problem/1264
while True:
    n = input()

    if n == "#":
        break

    count = 0

    for m in n.lower():
        if m in "aeiou":
            count += 1

    print(count)

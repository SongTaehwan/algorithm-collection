# https://www.acmicpc.net/problem/5355
for _ in range(int(input())):
    num, *ops = list(input().split())
    num = float(num)

    for o in ops:
        if o == "@":
            num *= 3
        elif o == "%":
            num += 5
        else:
            num -= 7

    print("{:.2f}".format(num))

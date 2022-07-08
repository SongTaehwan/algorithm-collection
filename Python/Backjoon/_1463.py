# https://www.acmicpc.net/problem/1463
value = int(input())
count = 0


while value != 1:
    count += 1

    if value % 3 == 0:
        value //= 3
    elif value % 3 == 1:
        value -= 1
    elif value % 2 == 0:
        value //= 2
    else:
        value -= 1

print(count)

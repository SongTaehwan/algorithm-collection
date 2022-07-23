# https://www.acmicpc.net/problem/23795

result = 0

while True:
    num = int(input())

    if num == -1:
        break

    result += num

print(result)

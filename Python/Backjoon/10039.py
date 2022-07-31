# https://www.acmicpc.net/problem/10039
result = 0

for _ in range(5):
    num = int(input())

    if num < 40:
        result += 40
    else:
        result += num

print(result // 5)

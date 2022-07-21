# https://www.acmicpc.net/problem/10872
num = int(input())

result = 1

while num > 0:
    result *= num
    num -= 1

print(result)

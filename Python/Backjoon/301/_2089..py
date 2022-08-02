# https://www.acmicpc.net/problem/2089
num = int(input())

result = ""

while num != -1:
    result += str(num % 2)
    num //= 2

print(result)

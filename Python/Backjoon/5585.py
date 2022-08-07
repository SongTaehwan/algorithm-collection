# https://www.acmicpc.net/problem/5585
m = 1000 - int(input())

result = 0
result += m // 500
m %= 500
result += m // 100
m %= 100
result += m // 50
m %= 50
result += m // 10
m %= 10
result += m // 5
m %= 5
result += m // 1

print(result)

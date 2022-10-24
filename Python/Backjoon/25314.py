# https://www.acmicpc.net/problem/25314
n = int(input()) // 4
result = ""

for _ in range(n):
    result += "long "

print(result + "int")

# https://www.acmicpc.net/problem/25640
n = input()

count = 0

for _ in range(int(input())):
    if n == input():
        count += 1

print(count)

# https://www.acmicpc.net/problem/8393
sum = 0

for i in range(1 + int(input())):
    sum += i

print(sum)

# Refactor
count = range(int(input()) + 1)
print(sum(count))  # range 를 합할 수 있음

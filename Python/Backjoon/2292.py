# https://www.acmicpc.net/problem/2292
n = int(input())

count = 1
room = 1

while room < n:
    room += 6 * count
    count += 1

print(count)

# other
n = int(input())

count = 1

while n > 1:
    n -= 6 * count
    count += 1

print(count)

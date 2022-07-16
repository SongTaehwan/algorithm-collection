# https://www.acmicpc.net/problem/1110
origin = int(input())
number = origin
count = 0

while True:
    count += 1
    front = number // 10
    back = number % 10
    sum = front + back
    number = int(str(back) + str(sum % 10))

    if origin == number:
        break

print(count)

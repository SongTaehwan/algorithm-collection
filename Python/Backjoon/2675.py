# https://www.acmicpc.net/problem/2675
count = int(input())

for i in range(count):
    repeat, string = input().split()

    result = ""

    for char in string:
        result += char * int(repeat)

    print(result)

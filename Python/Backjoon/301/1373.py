# https://www.acmicpc.net/problem/1373
bits = list(input())

result = ""
square = 0
sum = 0

while len(bits) > 0:
    binary = bits.pop()

    if binary == "1":
        sum += 2 ** square

    square += 1

    if square % 3 == 0 or len(bits) == 0:
        result = str(sum) + result
        square = 0
        sum = 0

print(result)

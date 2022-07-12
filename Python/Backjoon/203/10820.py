# https://www.acmicpc.net/problem/10820
def isLower(value):
    point = ord(value)
    return point >= 97 and point <= 122


def isUpper(value):
    point = ord(value)
    return point >= 65 and point <= 90


def isDecimal(value):
    point = ord(value)
    return point >= 48 and point <= 57


def isSpace(value):
    point = ord(value)
    return point == 32


while True:
    try:
        result = [0, 0, 0, 0]

        for i in input():
            if isLower(i):
                result[0] += 1
            elif isUpper(i):
                result[1] += 1
            elif isDecimal(i):
                result[2] += 1
            elif isSpace(i):
                result[3] += 1

        print(*result)
    except:
        break

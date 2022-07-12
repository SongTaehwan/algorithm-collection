# https://www.acmicpc.net/problem/11655

def isLowerCase(char: str):
    point = ord(char)
    return point >= 97 and point <= 122


def isUpperCase(char: str):
    point = ord(char)
    return point >= 65 and point <= 90


result = ""

for char in input():
    point = ord(char)
    update = point + 13

    if isLowerCase(char):
        code = update % 122 + 96 if update > 122 else update
        result += chr(code)
    elif isUpperCase(char):
        code = update % 90 + 64 if update > 90 else update
        result += chr(code)
    else:
        result += char

# print(result)

# Refactor
for i in input():
    if i.islower():
        point = ord(i) + 13

        if point > 122:
            # 초과하는 부분이 처음 시작 부분에서 몇번째인지 알아내는 방법에는 2가지가 있다.
            # 1. % 연산 // 몇번째 인지까지만 알려줌
            # 2. 전체 크기만큼 뺄셈 // 특정 위치값을 기준으로 몇번째인지 알 수 있음
            point -= 26
        print(chr(point), end="")
    elif i.isupper():
        point = ord(i) + 13

        if point > 90:
            point -= 26

        print(chr(point), end="")
    else:
        print(i, end="")

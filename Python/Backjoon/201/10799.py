# https://www.acmicpc.net/problem/10799

# 실제로 레이저로 잘랐을 때 왼쪽에 잘린 것만 모아서 개수를 세는 그림을 떠올려볼 것
stack = list()
result = 0

for i, char in enumerate(input()):
    if char == "(":
        stack.append(i)
    elif char == ")":
        if i - stack[-1] == 1:
            stack.pop()
            bars = len(stack)  # 레이저가 자른 바의 개수
            result += bars
        else:
            stack.pop()
            result += 1  # 자른 바의 개수 + 나머지 한 조각

print(result)

# Refactor

string = input().replace("()", "0")
bars = 0
result = 0

for char in string:
    if char == "(":
        bars += 1
    elif char == "0":
        result += bars
    else:
        bars -= 1  # 다 잘랐으니 막대기 제외
        result += 1  # 다 자른 뒤 남은 한조각

print(result)  # O(n)

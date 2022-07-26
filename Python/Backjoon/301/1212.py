# https://www.acmicpc.net/problem/1212
nums = map(int, list(input()))
stack = list()
result = list()

for oct in nums:
    if oct == 0 and len(result) == 0:
        result.append("0")
        break

    while oct > 0:
        m = oct % 2
        stack.append(str(m))
        oct //= 2

    while len(stack) == 0 or len(stack) % 3 != 0:
        stack.append("0")

    while len(stack) != 0:
        num = stack.pop()

        if len(result) == 0 and num == "0":
            continue

        result.append(num)

print("".join(result))

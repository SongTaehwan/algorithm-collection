# https://www.acmicpc.net/problem/1874
count = int(input())
stack = list()
result = list()
last = 0

while count:
    number = int(input())

    if number > last:
        while number > last:
            last += 1
            stack.append(last)
            result.append("+")

        stack.pop()
        result.append("-")
    else:
        found = False

        if len(stack) != 0:
            top = stack[-1]
            stack.pop()
            result.append("-")

            if number == top:
                found = True

        if not found:
            result = ["NO"]
            break

    count -= 1

print(*result, sep="\n")

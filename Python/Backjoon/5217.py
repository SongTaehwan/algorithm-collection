# https://www.acmicpc.net/problem/5217
for _ in range(int(input())):
    num = int(input())

    i = 1

    result = f"Pairs for {num}: "
    stack = []

    while True:
        rest = num - i

        if i >= rest:
            break

        stack.append(f"{i} {rest}")

        i += 1

    print(result + ", ".join(stack))

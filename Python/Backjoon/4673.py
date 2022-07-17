# https://www.acmicpc.net/problem/4673

def solve(n: int) -> int:
    num = n

    while n > 0:
        num += n % 10
        n //= 10

    return num


stack = list()

for i in range(1,  10001):
    stack.append(solve(i))

for i in range(1,  10001):
    if i not in stack:
        print(i)

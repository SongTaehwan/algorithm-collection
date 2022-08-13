# https://www.acmicpc.net/problem/2748

def fibonacci(n: int) -> int:
    global memo

    if n <= 2:
        return 1
    else:
        if not memo[n]:
            memo[n] = fibonacci(n-1) + fibonacci(n-2)

        return memo[n]


n = int(input())

memo = [0] * (n + 1)

print(fibonacci(n))

# Refactor with for loop

n = int(input())
memo = [0, 1, 1]


def fibonacci(n: int) -> int:
    for i in range(3, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]


print(fibonacci(n))

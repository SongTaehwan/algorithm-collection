# https://www.acmicpc.net/problem/10870

def fibonacci(n: int) -> int:
    global memo

    if n <= 2:
        return 1
    else:
        if not memo[n]:
            memo[n] = fibonacci(n-1) + fibonacci(n-2)

        return memo[n]


n = int(input())

if n == 0:
    print(0)
else:
    memo = [0, 1, 1] + [0] * (n - 2)
    print(fibonacci(n))

# Refactor with out memoization and for loop


def fibonacci(n: int) -> int:
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a


print(fibonacci(int(input())))

# Simpler version
n = int(input())
a = 0
b = 1

for _ in range(n):
    a, b = b, a + b

print(a)

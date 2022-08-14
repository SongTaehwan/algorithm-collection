# https://www.acmicpc.net/problem/24416

def fibonacci(n: int) -> int:
    global memo

    if n <= 2:
        return 1
    else:
        if not memo[n]:
            memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]


n = int(input())
memo = [0, 1] + [0] * (n-1)
print(fibonacci(n), n - 2)

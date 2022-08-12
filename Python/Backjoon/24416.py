# https://www.acmicpc.net/problem/24416

def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input())
print(fibonacci(n), n - 2)

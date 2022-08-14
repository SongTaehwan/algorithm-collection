# https://www.acmicpc.net/problem/17175
# 재귀함수 호출 횟수는 n-2 호출 횟수 + n-1 호출 횟수
def fibonacci(n):
    global memo

    if n < 2:
        # n = 0, 1 모두 호출 횟수는 1
        return 1
    else:
        if not memo[n]:
            # 자기 자신의 호출 회수 + n-1 + n-2 의 호출 회수
            memo[n] = (1 + fibonacci(n-1) + fibonacci(n-2)) % 1000000007

        return memo[n]


n = int(input())
memo = [1, 1] + [0] * (n-1)  # 호출 회수를 담음

fibonacci(n)
print(memo[n])

# with loop
n = int(input())

a, b = 1, 1

for _ in range(n):
    a, b = b, (1+a+b) % 1000000007
print(a)

# https://www.acmicpc.net/problem/2775
# Top-down
def go(k, n):
    global memo

    if k == 0:
        return n

    key = f"{k}-{n}"

    if key in memo:
        return memo[key]

    result = 0

    for i in range(1, n + 1):
        result += go(k-1, i)

    memo[key] = result

    return memo[key]


memo = {}


for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(go(k, n))

# Bottom-up
for _ in range(int(input())):
    k = int(input())
    n = int(input())

    residence = [i for i in range(n+1)]

    for i in range(k):
        for j in range(2, n + 1):
            residence[j] = residence[j] + residence[j-1]

    print(residence[-1])

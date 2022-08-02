# https://www.acmicpc.net/problem/17087
def gcd(a, b) -> int:
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


n, s = map(int, input().split())
p = list(map(int, input().split()))

stack = []

for a in p:
    stack.append(abs(s-a))

result = stack[0]

# 세 수의 최대공약수는 앞의 두 수의 최대공약수와 그 다음 수와의 최대공약수이다. N 개면 N-1 반복
for i in range(1, n):
    result = gcd(result, stack[i])

print(result)

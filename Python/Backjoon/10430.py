# https://www.acmicpc.net/problem/10430

a, b, c = map(int, input().split())
print(
    (a + b) % c,
    ((a % c) + (b % c)) % c,
    (a * b) % c,
    ((a % c) * (b % c)) % c,
    sep='\n'
)

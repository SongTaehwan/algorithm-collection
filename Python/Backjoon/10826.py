# https://www.acmicpc.net/problem/10826
a, b = 0, 1

for _ in range(int(input())):
    a, b = b, a + b

print(a)

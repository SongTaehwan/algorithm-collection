# https://www.acmicpc.net/problem/2720
import sys

for _ in range(int(input())):
    m = int(sys.stdin.readline())

    q = 0
    d = 0
    n = 0

    q += m // 25
    m %= 25
    d += m // 10
    m %= 10
    n += m // 5
    m %= 5

    print(q, d, n, m)

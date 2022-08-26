# https://www.acmicpc.net/problem/11557
import sys

for _ in range(int(sys.stdin.readline())):
    amount = 0
    winner = ""

    for _ in range(int(sys.stdin.readline())):
        a, b = sys.stdin.readline().split()
        b = int(b)

        if b > amount:
            winner = a
            amount = b

    print(winner)

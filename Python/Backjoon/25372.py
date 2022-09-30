# https://www.acmicpc.net/problem/25372
import sys


for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().strip()

    if len(n) >= 6 and len(n) <= 9:
        print("yes")
    else:
        print("no")

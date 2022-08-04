# https://www.acmicpc.net/problem/9086
import sys

for _ in range(int(input())):
    word = sys.stdin.readline().rstrip()

    print(word[0] + word[-1])

# https://www.acmicpc.net/problem/15552
import sys

count = int(input())

for i in range(count):
    print(sum(map(int, sys.stdin.readline().split())))

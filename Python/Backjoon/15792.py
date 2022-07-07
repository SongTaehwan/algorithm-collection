# https://www.acmicpc.net/problem/15792
import sys

a, b = map(int, sys.stdin.readline().split())
result = a / b
print(f'{result:.2000f}')

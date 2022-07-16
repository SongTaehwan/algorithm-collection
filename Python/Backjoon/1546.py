# https://www.acmicpc.net/problem/1546
import sys

length = int(input())
array = list(map(int, sys.stdin.readline().split()))

m = max(array)
sum = sum(array) / m * 100

print(sum / length)

# https://www.acmicpc.net/problem/10815
import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

dictionary = dict()
s = card + nums

for n in s:
    dictionary.setdefault(n, -1)
    dictionary[n] += 1


for num in nums:
    print(dictionary[num], end=" ")

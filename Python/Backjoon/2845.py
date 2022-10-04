# https://www.acmicpc.net/problem/2845
l, p = map(int, input().split())
nums = list(map(int, input().split()))
n = l * p

for num in nums:
    print(num - n, end=" ")

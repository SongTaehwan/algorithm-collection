# https://www.acmicpc.net/problem/13597
A, B = map(int, input().split())
print(A if A == B else max(A, B))

# https://www.acmicpc.net/problem/24480
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
adjacencyList = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)

for item in adjacencyList:
    item.sort(reverse=True)

visited = [0] * (n + 1)
count = 1


def dfs(x: int, c: int):
    global count
    visited[x] = c

    for i in adjacencyList[x]:
        if visited[i] == 0:
            count += 1
            dfs(i, count)


dfs(r, count)

for i in range(1, n+1):
    print(visited[i])

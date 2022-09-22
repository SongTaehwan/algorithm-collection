# https://www.acmicpc.net/problem/24479
import sys

sys.setrecursionlimit(10**6)

# DFS - Adjacency Matrix


def dfs(x: int, c: int):
    global count
    visited[x] = c

    for i in range(1, n+1):
        if matrix[x][i] == 1 and visited[i] == 0:
            count += 1
            dfs(i, count)


n, m, r = map(int, input().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

count = 1
dfs(r, count)

for i in range(1, n+1):
    print(visited[i])

# DFS - Adjacency List

n, m, r = map(int, sys.stdin.readline().split())
aList = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    aList[u].append(v)
    aList[v].append(u)

for item in aList:
    item.sort()

count = 1


def dfs(x: int, c: int):
    global count
    visited[x] = c

    for i in range(len(aList[x])):
        v = aList[x][i]

        if visited[v] == 0:
            count += 1
            dfs(v, count)


dfs(r, count)

for i in range(1, n+1):
    print(visited[i])

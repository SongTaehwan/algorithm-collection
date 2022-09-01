# https://www.acmicpc.net/problem/1260
import sys

# 인접 행렬 - DFS
v, m, s = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(v + 1)] for _ in range(v+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

check = [False] * (v + 1)
check[s] = True
dfs_result = [s]


def dfs(n: int):
    check[n] = True

    # 정점 개수만큼 순회
    for i in range(1, v+1):
        if matrix[n][i] == 1 and check[i] == False:
            dfs_result.append(i)
            dfs(i)


dfs(s)

print(*dfs_result)

# 인접 행렬 - BFS
check = [False] * (v + 1)
check[s] = True
queue = [s]
bfs_result = []

while queue:
    x = queue.pop(0)
    bfs_result.append(x)

    # 모든 정점 순회
    for i in range(1, v+1):
        if matrix[x][i] == 1 and check[i] == False:
            check[i] = True
            queue.append(i)

print(*bfs_result)

# 인접 리스트

v, m, s = map(int, sys.stdin.readline().split())

aList = [[] for _ in range(v+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향
    aList[a].append(b)
    aList[b].append(a)

# 간선이 어려개면 작은 것부터 방문(문제조건)
for item in aList:
    item.sort()

check = [False] * (v+1)
check[s] = True
dfs_result = [s]


def dfs(n: int):
    check[n] = True

    for i in range(len(aList[n])):
        v = aList[n][i]

        if check[v] == False:
            dfs_result.append(v)
            dfs(v)


dfs(s)


print(*dfs_result)

# BFS
check = [False] * (v+1)
check[s] = True
bfs_result = []
queue = [s]

while queue:
    x = queue.pop(0)
    bfs_result.append(x)

    for i in range(len(aList[x])):
        y = aList[x][i]

        if check[y] == False:
            check[y] = True
            queue.append(y)

print(*bfs_result)

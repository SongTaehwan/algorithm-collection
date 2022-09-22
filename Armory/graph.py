# Graph
import sys

# DFS - 인접 행렬
n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n+1)]

for _ in range(int(m)):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

check = [False] * (n+1)


def dfs(x: int):
    check[x] = True

    for i in range(1, n+1):
        if matrix[x][i] == 1 and check[i] == False:
            dfs(i)


# DFS - 인접 리스트
n, m = map(int, sys.stdin.readline().split())
aList = [[] for _ in range(n+1)]

for _ in range(int(m)):
    a, b = map(int, sys.stdin.readline().split())
    aList[a].append(b)
    aList[b].append(a)

# 탐색 - DFS
check = [False] * (n+1)


def dfs(x: int):
    check[x] = True

    for i in range(len(aList[x])):
        v = aList[x][i]

        if check[v] == False:
            dfs(v)


# BFS - 인접 행렬
n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n + 1)] for _ in range(n+1)]

for _ in range(int(m)):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

# 그래프 탐색 - BFS
queue = [1]  # 1 부터 탐색을 시작한다고 가정
check = [False] * (n+1)  # 정점 개수만큼
check[1] = True
result = 0

while queue:
    x = queue.pop(0)

    for i in range(1, n+1):
        if matrix[x][i] == 1 and check[i] == False:
            check[i] = True
            queue.append(i)
            result += 1

# BFS - 인접 리스트
n, m = map(int, sys.stdin.readline().split())
aList = [[] for _ in range(n+1)]

for _ in range(int(m)):
    a, b = map(int, sys.stdin.readline().split())
    aList[a].append(b)
    aList[b].append(a)

check = [False] * (n+1)
check[1] = True
queue = [1]

while queue:
    x = queue.pop(0)

    for i in range(len(aList[x])):
        v = aList[x][i]

        if check[v] == False:
            check[v] = True
            queue.append(v)

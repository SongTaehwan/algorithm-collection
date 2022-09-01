# https://www.acmicpc.net/problem/9372
# 국가 n => 정점
# 비행기 m => 간선
import sys

# 인접 행렬 - Adjacency matrix
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(n + 1)] for _ in range(n+1)]

    for _ in range(int(m)):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = 1
        matrix[b][a] = 1

    # 그래프 탐색 - BFS
    queue = [1]
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

    print(result)

    check = [False] * (n+1)
    result = 0

    # 그래프 탐색 - DFS
    def dfs(x: int):
        global result
        check[x] = True

        for i in range(1, n+1):
            if matrix[x][i] == 1 and check[i] == False:
                result += 1
                dfs(i)

        dfs(1)
        print(result)


# 인접 리스트 - Adjacency list
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    aList = [[] for _ in range(n+1)]

    for _ in range(int(m)):
        a, b = map(int, sys.stdin.readline().split())
        aList[a].append(b)
        aList[b].append(a)

    # 탐색 - DFS
    check = [False] * (n+1)
    result = 0

    def dfs(x: int):
        global result
        check[x] = True

        for i in range(len(aList[x])):
            v = aList[x][i]

            if check[v] == False:
                result += 1
                dfs(v)
    dfs(1)
    print(result)

    # 탐색 - BFS
    check = [False] * (n+1)
    check[1] = True
    result = 0
    queue = [1]

    while queue:
        x = queue.pop(0)

        for i in range(len(aList[x])):
            v = aList[x][i]

            if check[v] == False:
                result += 1
                check[v] = True
                queue.append(v)

    print(result)

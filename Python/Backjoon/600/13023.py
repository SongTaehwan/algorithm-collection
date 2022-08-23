# https://www.acmicpc.net/problem/13023
# A-B, C-D => 간선 리스트
# B-C => 인접 행렬
# D-E => 인접 리스트
import sys

n, m = map(int, sys.stdin.readline().split())

adjacencyMatrix = []
adjacencyList = []
edgeList = []

for i in range(n):
    adjacencyMatrix.append([])

    for j in range(n):
        adjacencyMatrix[i].append(False)

for _ in range(n):
    adjacencyList.append([])

for _ in range(m):
    # a, b 는 인덱스
    a, b = map(int, sys.stdin.readline().split())

    # 간선 리스트
    edgeList.append((a, b))
    edgeList.append((b, a))

    # 인접 행렬
    adjacencyMatrix[a][b] = True
    adjacencyMatrix[b][a] = True

    # 인접 리스트
    adjacencyList[a].append(b)
    adjacencyList[b].append(a)

# 친구 관계는 양방향이므로 간선의 개수는 입력의 2배
# ABCDE 검증

for i in range(m*2):
    for j in range(m*2):
        # A - B
        a, b = edgeList[i]

        # C - D
        c, d = edgeList[j]

        if a == b or a == c or a == d or b == c or b == d or c == d:
            continue

        # B -> C
        if not adjacencyMatrix[b][c]:
            continue

        # D -> E
        for e in adjacencyList[d]:
            if e == a or e == b or e == c or e == d:
                continue

            print(1)
            sys.exit()

print(0)

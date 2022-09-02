# https://www.acmicpc.net/problem/16173
# 브루트포스
# import sys
# n = int(input())

# gameMap = [[0, 0, 0]]

# for _ in range(n):
#     gameMap.append([0]+list(map(int, input().split())))

# row = 1
# column = 1

# reachable = False

# while column <= n:
#     while row <= n:
#         if row == n and column == n:
#             reachable = True
#             break

#         weight = gameMap[column][row]

#         if row + weight <= n:
#             row += weight
#             continue
#         elif weight + column + 1 <= n:
#             column += weight
#             continue
#         else:
#             row -= 1

#         column += 1
#         break

#     if row == n and column == n:
#         break


# print("Hing" if not reachable else "HaruHaru")

# # DFS
# n = int(sys.stdin.readline())
# matrix = []

# for _ in range(n):
#     matrix.append(list(map(int, sys.stdin.readline().split())))


# def dfs(x, y):
#     if x >= n or y >= n:
#         return False

#     if x == n-1 and y == n-1:
#         return True

#     move = matrix[x][y]

#     if move == 0:
#         return False
#     # 오른쪽, 아래쪽 각각 검사
#     return (dfs(x + move, y) or dfs(x, y + move))


# if dfs(0, 0):
#     print("HaruHaru")
# else:
#     print("Hing")

# BFS
n = int(input())
gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

queue = [[0, 0]]
reachable = False

while queue:
    x, y = queue.pop(0)

    if x >= n or y >= n:
        break

    if x == n-1 and y == n-1:
        reachable = True
        break

    if gameMap[x][y] == 0:
        break

    if n > x + gameMap[x][y] and y < n:
        queue.append([x + gameMap[x][y], y])

    if n > x and y + gameMap[x][y] < n:
        queue.append([x, y + gameMap[x][y]])

print("HaruHaru" if reachable else "Hing")

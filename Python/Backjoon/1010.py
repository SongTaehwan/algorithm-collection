# https://www.acmicpc.net/problem/1010
# 참고.1 https://codedrive.tistory.com/284
# 참고.2 https://velog.io/@uoayop/BOJ-1010-다리-놓기Python
# D[n][m] = D[n-1][m-1] + D[n-1][m-2] + D[n-1][m-3] + ... + D[n-1][n-1]
import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())

    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    d[1] = [i for i in range(m+1)]

    # 서쪽 다리 i
    for i in range(2, n+1):
        # 동쪽 다리 j
        # i <= j
        for j in range(i, m+1):
            # 동쪽 다리 k 가 i 와 같거나 커야함
            for k in range(j, i-1, -1):
                # D[n-1][m-1] + D[n-1][m-2] + ... + D[n-1][n-1]
                d[i][j] += d[i-1][k-1]

    print(d[n][m])

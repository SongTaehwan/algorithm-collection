# https://www.acmicpc.net/problem/2309
import sys

n = []

for i in range(9):
    n.append(int(sys.stdin.readline()))

n.sort()

# 9명 중 7명의 키를 제외한 나머지 2명의 합
s = sum(n) - 100
done = False

for i in range(8):
    for j in range(i + 1, 9):
        a = n[i]
        b = n[j]

        if a+b == s:
            n.remove(a)
            n.remove(b)
            done = True
            break

    if done:
        break

print(*n, sep="\n")

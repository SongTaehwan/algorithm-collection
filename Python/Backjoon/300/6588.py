# https://www.acmicpc.net/problem/6588
# 에라토스테네스의 체 (set)
import sys

check = set(range(2, 1000001))

for i in range(2, 1000001):
    if i in check:
        check -= set(range(i * i, 1000001, i))


while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    found = False

    for i in check:
        if n - i in check:
            found = True
            print(f"{n} = {i} + {n-i}")
            break

    if found == False:
        print("Goldbach's conjecture is wrong.")

# 에라토스테네스의 체 (for loop) -> set 보다 빠름
check = [True] * 1000001

for i in range(2, 1000001):
    if check[i]:

        for j in range(i * i, 1000001, i):
            check[j] = False

while True:
    n = int(sys.stdin.readline())

    if not n:
        break

    found = False

    for i in range(3, n):  # 문제에서 홀수라고 조건이 주어졌기 때문에 3부터 시작
        if check[i] and check[n - i]:
            print(f"{n} = {i} + {n-i}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")

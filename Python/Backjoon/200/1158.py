# https://www.acmicpc.net/problem/1158
from collections import deque
import sys

count, nth = map(int, sys.stdin.readline().split())

rest = deque(range(1, count + 1))
dead = list()
pointer = nth

while rest:
    target = rest.popleft()

    if pointer == 1:
        dead.append(str(target))
        pointer = nth
    else:
        rest.append(target)
        pointer -= 1

print(f'<{", ".join(dead)}>')

# Refactor
count, nth = map(int, sys.stdin.readline().split())
rest = list(range(1, count + 1))
dead = list()

index = 0

while rest:
  # 8 % 7 = 1 길이를 초과한 인덱스 값을 얻을 수 있음...😭
    index = (index + nth - 1) % len(rest)
    dead.append(str(rest.pop(index)))

print(f'<{", ".join(dead)}>')

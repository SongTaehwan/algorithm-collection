# https://www.acmicpc.net/problem/8958
import sys

for i in range(int(input())):
    quiz = sys.stdin.readline()
    bonus = 0
    score = 0

    for i in quiz:
        if i == "O":
            score += 1 + bonus
            bonus += 1
        else:
            bonus = 0

    print(score)

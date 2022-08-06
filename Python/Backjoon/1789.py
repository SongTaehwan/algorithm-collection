# https://www.acmicpc.net/problem/1789
# 1+2+3+…+19 = 190 이고, 1+2+3+…+20 = 210
# 1+2+3+…+17+18+19 가 아니라 1+2+3+…+17+18+29 로 바꾸면
# 200을 만들 수 있으며 더한 숫자의 갯수는 19개

s = int(input())

i = 1
count = 0

while s > 0:
    if s - i < 0:
        break

    count += 1
    s -= i
    i += 1

print(count)

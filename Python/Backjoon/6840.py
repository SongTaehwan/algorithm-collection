# https://www.acmicpc.net/problem/6840
size = [int(input()), int(input()), int(input())]

for n in size:
    if n < max(size) and n > min(size):
        print(n)

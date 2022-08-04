# https://www.acmicpc.net/problem/2744
word = input()

for char in word:
    if char.islower():
        print(char.upper(), end="")
    else:
        print(char.lower(), end="")

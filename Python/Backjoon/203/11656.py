# https://www.acmicpc.net/problem/11656

string = input()

stack = list()
length = len(string)

for i in range(0, length):
    stack.append(string[i:length])

stack.sort()
print(*stack, sep="\n")

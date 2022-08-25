# https://www.acmicpc.net/problem/14487
int(input())
w = list(map(int, input().split()))

print(sum(w) - max(w))

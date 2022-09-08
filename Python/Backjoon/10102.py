# https://www.acmicpc.net/problem/10102
s = int(input())
a = 0

for i in list(input()):
    if i.upper() == "A":
        a += 1

if a > abs(s-a):
    print("A")
elif a == abs(s-a):
    print("Tie")
else:
    print("B")

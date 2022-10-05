# https://www.acmicpc.net/problem/15873
n = input()

if int(n[-2::]) == 10:
    a = int(n[:-2])
    b = 10
    print(a+b)
else:
    a = int(n[:-1])
    b = int(n[-1])
    print(a+b)

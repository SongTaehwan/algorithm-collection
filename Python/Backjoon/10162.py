time = int(input())

a = 0
b = 0
c = 0

a += time // 300
time = time % 300
b += time // 60
time = time % 60
c += time // 10
time = time % 10

if time > 0:
    print(-1)
else:
    print(a, b, c)

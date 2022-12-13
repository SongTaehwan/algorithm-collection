# https://www.acmicpc.net/problem/2083
while True:
    name, age, weight = input().split()

    if name == '#':
        break

    if int(age) > 17 or int(weight) >= 80:
        print("%s Senior" % name)
    else:
        print("%s Junior" % name)

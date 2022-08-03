# https://www.acmicpc.net/problem/2920
notes = list(map(int, input().split()))

asc = 1
des = 1
count = len(notes)
num = notes.pop()

while notes:
    target = notes.pop()

    if num - target == 1:
        asc += 1
    elif num - target == -1:
        des += 1
    else:
        print("mixed")
        break

    num = target

if asc == count:
    print("ascending")

if des == count:
    print("descending")

# refactor
notes = "".join(input().split())

if notes == "12345678":
    print("ascending")
elif notes == "87654321":
    print("descending")
else:
    print("mixed")

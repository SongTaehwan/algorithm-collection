# https://www.acmicpc.net/problem/5622
dial = list(input())
time = 0

for char in dial:
    if char in "ABC":
        time += 3
    elif char in "DEF":
        time += 4
    elif char in "GHI":
        time += 5
    elif char in "JKL":
        time += 6
    elif char in "MNO":
        time += 7
    elif char in "PQRS":
        time += 8
    elif char in "TUV":
        time += 9
    elif char in "WXYZ":
        time += 10

print(time)

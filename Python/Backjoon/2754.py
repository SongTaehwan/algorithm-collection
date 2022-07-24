# https://www.acmicpc.net/problem/2754
grade = input()

result = 0.0

if grade.count("A"):
    result = 4.0
elif grade.count("B"):
    result = 3.0
elif grade.count("C"):
    result = 2.0
elif grade.count("D"):
    result = 1.0

if grade.count("+"):
    result += 0.3
elif grade.count("-"):
    result -= 0.3

print(result)

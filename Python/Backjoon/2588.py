a = int(input())
b = int(input())

divide = 10
result = a * b

while b != 0:
    value = b % divide
    b = b // divide
    print(a * value)

print(result)

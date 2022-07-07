# def getInput():
#     return input().split()


# def parseInt(collection):
#     return map(int, collection)


# while True:
#     try:
#         numbers = list(parseInt(getInput()))

#         if len(numbers) > 1:
#             print(sum(numbers))
#     except EOFError:
#         break

# Refactor
count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    print(a + b)

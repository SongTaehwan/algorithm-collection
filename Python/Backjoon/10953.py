# while True:
#     try:
#         numbers = list(map(int, input().split(",")))

#         if len(numbers) < 2:
#             continue

#         result = sum(numbers)

#         if (result > 0):
#             print(result)
#     except:
#         break

# Refactor
count = int(input())

for i in range(count):
    numbers = map(int, input().split(","))
    result = sum(numbers)

    if not result:
        break

    print(result)

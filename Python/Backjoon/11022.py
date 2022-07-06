# number = 1

# while True:
#     try:
#         data = list(map(int, input().split()))

#         if len(data) < 2:
#             continue

#         a, b = data
#         sum = a + b

#         if sum > 0:
#             print(f'Case #{number}: {a} + {b} = {sum}')
#             number += 1
#     except:
#         break

# Refactor
count = int(input())

for i in range(1, count + 1):
    a, b = map(int, input().split())

    if a + b < 0:
        break

    print(f'Case #{i}: {a} + {b} = {a + b}')

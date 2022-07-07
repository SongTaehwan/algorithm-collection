# number = 1

# while True:
#     try:
#         data = list(map(int, input().split()))

#         if len(data) < 2:
#             continue

#         result = sum(data)

#         if result > 0:
#             print(f'Case #{number}: {result}')
#             number += 1
#     except:
#         break

# Refactor
count = int(input())

for i in range(1, count + 1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a + b}')

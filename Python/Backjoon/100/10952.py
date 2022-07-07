# while True:
#     try:
#         a, b = map(int, input().split())
#         sum = a + b

#         if (sum > 0):
#             print(a + b)
#     except:
#         break

# Refactor
while True:
    a, b = map(int, input().split())
    sum = a + b

    if (sum > 0):  # 에러를 통해 브래이크되는 것은 좋지 않음
        print(a + b)
    else:
        break

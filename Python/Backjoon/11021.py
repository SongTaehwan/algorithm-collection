number = 1

while True:
    try:
        data = list(map(int, input().split()))

        if len(data) < 2:
            continue

        result = sum(data)

        if result > 0:
            print(f'Case #{number}: {result}')
            number += 1
    except:
        break

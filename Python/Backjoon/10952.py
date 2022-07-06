while True:
    try:
        a, b = map(int, input().split())
        sum = a + b

        if (sum > 0):
            print(a + b)
    except:
        break

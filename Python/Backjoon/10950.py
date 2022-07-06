def getInput():
    return input().split()


def parseInt(collection):
    return map(int, collection)


while True:
    try:
        numbers = list(parseInt(getInput()))

        if len(numbers) > 1:
            print(sum(numbers))
    except EOFError:
        break

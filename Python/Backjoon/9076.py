# https://www.acmicpc.net/problem/9076
def mergeSort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


for _ in range(int(input())):
    n = list(map(int, input().split()))
    mergeSort(n)
    n.pop()
    n.pop(0)

    if n[len(n)-1] - n[0] >= 4:
        print("KIN")
    else:
        print(sum(n))

# https://www.acmicpc.net/problem/5576
def quickSort(arr: list[int], start: int, end: int):
    def partition(arr: list[int], start: int, end: int):
        pivot = arr[(start + end) // 2]
        left = start
        right = end

        while left <= right:
            while pivot > arr[left]:
                left += 1
            while pivot < arr[right]:
                right -= 1

            if left <= right:
                # Swap
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1

        return left

    if start < end:
        index = partition(arr, start, end)
        quickSort(arr, start, index - 1)
        quickSort(arr, index, end)


w = 0
s = [int(input()) for _ in range(10)]
quickSort(s, 0, len(s)-1)
w += sum(s[-3:])

k = 0
s = [int(input()) for _ in range(10)]
quickSort(s, 0, len(s)-1)
k += sum(s[-3:])

print(w, k)

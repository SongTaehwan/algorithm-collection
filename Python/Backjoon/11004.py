# https://www.acmicpc.net/problem/11004
import sys


# Merge Sort
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


# Quick Sort
def quickSort(arr: list[int], start: int, end: int):
    def partition(arr: list[int], start: int, end: int) -> int:
        mid = (start + end) // 2
        pivot = arr[mid]

        def swap(arr: list[int], start: int, end: int):
            temp = arr[end]
            arr[end] = arr[start]
            arr[start] = temp

        while start <= end:
            while arr[start] < pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start <= end:
                swap(arr, start, end)
                # start == end 일 때 크기는 start > end 로 역전됨
                start += 1
                end -= 1

        return start  # 대칭되는 sub array 의 시작 인덱스

    # Termination condition
    if start < end:
        # 하위 배열의 요소가 1개 일 때, start 와 end 는 같기 때문에
        # 정렬할 필요 없다. 따라서 start < end 경우에만 정렬한다.
        firstIndexOnRight = partition(arr, start, end)
        quickSort(arr, start, firstIndexOnRight - 1)
        quickSort(arr, firstIndexOnRight, end)


n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
# s.sort()
# mergeSort(s)
quickSort(s, 0, n-1)
print(s[k-1])

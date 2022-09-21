# https://www.acmicpc.net/problem/1181
import sys


def mergeSort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                arr[k] = left[i]
                i += 1
            elif left[i][0] == right[j][0] and left[i][1] < right[j][1]:
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


s = []

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().rstrip()
    s.append((len(n), n))

mergeSort(s)

w = ""

for d in s:
    if d[1] != w:
        w = d[1]
        print(w)

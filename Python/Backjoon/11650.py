# https://www.acmicpc.net/problem/11650
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
            lx = left[i][0]
            rx = right[j][0]
            ly = left[i][1]
            ry = right[j][1]

            if lx < rx:
                arr[k] = left[i]
                i += 1
            elif lx == rx and ly < ry:
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


input = sys.stdin.readline

s = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    s.append((x, y))

mergeSort(s)

for d in s:
    print(d[0], d[1])

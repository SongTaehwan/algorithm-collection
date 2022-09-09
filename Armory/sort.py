# Merge Sort - O(Nlog(N))
def mergeSort(items: list[int]):
    if len(items):
        # Divide whole into two
        middle = len(items) // 2
        left = items[:middle]
        right = items[middle:]

        mergeSort(left)
        mergeSort(right)

        # i for left, j for right, k for result
        i = j = k = 0

        # Merging operation
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1  # point to the next item in left
            else:
                items[k] = right[j]
                j += 1  # point to the next item in right
            k += 1

        # in case for remaining item in left or right
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1

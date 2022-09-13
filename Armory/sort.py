# Merge Sort - O(Nlog(N))
def mergeSort(items: list[int]):
    if len(items) > 1:
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


# Counting Sort - O(n+k)
def countingSort(array: list[int]):
    size = len(array)
    output = [0] * size
    count = [0] * 10  # 배열의 크기는 max(array) 에 따라 달라짐

    # 중복 수 개수 카운팅
    for num in array:
        count[num] += 1

    # 누적 수
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 1. 원본 배열(input) 요소의 정렬된 인덱스를 count 배열에서 찾는다.
    # 2. output 배열에 요소를 배치한다.
    i = 0

    while i < size:
        index = count[array[i]] - 1
        output[index] = array[i]
        count[array[i]] -= 1
        i += 1

    for i in range(size):
        array[i] = output[i]

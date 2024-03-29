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
    # 문제 조건에 따라 달라짐
    count = [0] * 10

    # 중복 수 카운팅
    # index = element in arr
    # value = 중복 횟수
    for num in array:
        count[num] += 1

    # 누적 수
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 1. 원본 배열(input) 요소의 정렬된 인덱스를 count 배열에서 찾는다.
    # 2. output 배열에 요소를 배치한다.
    i = 0

    while i < size:
        # 정렬된 배열(output)에서의 인덱스
        element = array[i]
        # 배열의 인덱스는 0 부터 시작하기 때문에 -1
        index = count[element] - 1
        # 정렬된 위치에 값을 저장
        output[index] = element
        # 중복 수 하나를 채우면 횟수 하나 차감
        count[element] -= 1
        i += 1

    for i in range(size):
        array[i] = output[i]


# Quick Sort - O(Nlog(N))
# 평균적인 경우에만 O(Nlog(N)) 이지 최악의 경우 O(N^2)
# 실질적으로는 Bubble Sort 보다 느림
def quickSort(array: list[int], start: int, end: int):
    def partition(array: list[int], start: int, end: int):
        # point for the element greater than pivot
        pointerForLeft = start
        # point for the element smaller than pivot
        pointerForRight = end
        pivot = array[(pointerForLeft + pointerForRight) // 2]

        while pointerForLeft <= pointerForRight:
            while array[pointerForLeft] < pivot:
                pointerForLeft += 1
            while array[pointerForRight] > pivot:
                pointerForRight -= 1

            if pointerForLeft <= pointerForRight:
                # Swap
                temp = array[pointerForLeft]
                array[pointerForLeft] = array[pointerForRight]
                array[pointerForRight] = temp
                # start == end 일 때 크기는 start > end 로 역전됨
                pointerForLeft += 1
                pointerForRight -= 1

        return pointerForLeft

    # Termination condition
    if start < end:
        # 하위 배열의 요소가 1개 일 때, start 와 end 는 같기 때문에
        # 정렬할 필요 없다. 따라서 start < end 경우에만 정렬한다.
        firstIndexOnRight = partition(array, start, end)
        quickSort(array, start, firstIndexOnRight - 1)
        quickSort(array, firstIndexOnRight, end)

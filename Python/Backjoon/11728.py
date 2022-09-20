# https://www.acmicpc.net/problem/11728
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Merge Sort 에 사용되는 방법
i = j = 0
result = []

while i < n and j < m:
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < n:
    result.append(a[i])
    i += 1

while j < m:
    result.append(b[j])
    j += 1

print(*result)

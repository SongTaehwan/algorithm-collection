# https://www.acmicpc.net/problem/9417
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    result = 0

    for i in range(len(nums) - 1):
        j = i + 1

        while j <= len(nums) - 1:
            result = max(result, gcd(nums[i], nums[j]))
            j += 1

    print(result)

# https://www.acmicpc.net/problem/9613
def gcd(a, b) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(int(input())):
    nums = list(map(int, input().split()))
    length = nums[0]
    nums = nums[1:]
    result = 0

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            result += gcd(nums[i], nums[j])

    print(result)

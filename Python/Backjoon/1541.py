# https://www.acmicpc.net/problem/1541
data = input()
nums = []

for char in data.split("-"):
    if "+" in char:
        # - 부호 뒤 이어 오는 모든 양수를 더해 음수를 최대값으로 만든 후 앞의 양수와 뺸다.
        # 55-(50+90)
        nums.append(sum(map(int, char.split("+"))))
    else:
        nums.append(int(char))

result = nums[0]

for i in range(1, len(nums)):
    result -= nums[i]

print(result)

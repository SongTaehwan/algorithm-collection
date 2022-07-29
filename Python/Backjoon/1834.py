# https://www.acmicpc.net/problem/1834
num = int(input())

result = 0

for i in range(1, num):
    # N - 1 = 조건에 맞는 값의 개수
    # 나머지와 몫이 같은 자연수는 배수 관계 (4, 8), (5, 10, 15)
    result += (num + 1) * i

print(result)

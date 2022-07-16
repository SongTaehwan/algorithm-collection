# https://www.acmicpc.net/problem/2577
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

number = a * b * c
dic = dict()

for i in range(10):
    dic.setdefault(i, 0)

for i in list(map(int, str(number))):
    dic[i] += 1

for i in range(10):
    print(dic[i])

# Another

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

array = list(map(int, str(a * b * c)))

for i in range(10):
    print(array.count(i))

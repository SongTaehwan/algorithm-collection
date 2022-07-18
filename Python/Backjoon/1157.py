# https://www.acmicpc.net/problem/1157
chars = input().upper()

dic = dict()

for char in chars:
    dic[char] = dic.get(char, 0) + 1

lst = list(dic.values())
lst.sort()

mx = lst.pop()
mxBf = lst.pop() if lst else 0

if mx == mxBf:
    print("?")
else:
    for (key, value) in dic.items():
        if value == mx:
            print(key)

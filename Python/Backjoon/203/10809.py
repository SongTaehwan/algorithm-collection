# https://www.acmicpc.net/problem/10809
dic = dict()

for point in range(97, 123):
    dic.setdefault(chr(point), -1)

for i, key in enumerate(input()):
    if dic.get(key) == -1:
        dic[key] = i

# insertion 순서를 보장하지만 스위프트 학습을 위해 안씀
for point in range(97, 123):
    print(dic.get(chr(point)), end=" ")

# https://www.acmicpc.net/problem/10808
dictionary = dict()

for i in range(97, 123):
    # list(string.ascii_lowercase) 보다 2배 빠름
    unicode = chr(i)
    dictionary.setdefault(unicode, 0)

for key in input():
    dictionary[key] += 1

# 파이썬의 Dictionary 는 3.7 부터 key 의 insertion 순서를 보장함
for key in dictionary:
    print(dictionary.get(key), end=" ")  # 꼭 문자열로 만들고 출력하지 않아도됌

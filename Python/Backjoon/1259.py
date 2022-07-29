# https://www.acmicpc.net/problem/1259
# Python 문자열 인덱스
# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
import sys

while True:
    num = sys.stdin.readline().rstrip()

    if num == "0":
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")

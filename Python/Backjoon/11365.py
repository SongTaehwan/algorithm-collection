# https://www.acmicpc.net/problem/11365
while True:
    sent = input()

    if sent == "END":
        break

    print(sent[::-1])

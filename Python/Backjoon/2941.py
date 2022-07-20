# https://www.acmicpc.net/problem/2941
string = input()
alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

result = 0

for i in alphabets:
    count = string.count(i)
    result += count

    if count > 0:
        string = string.replace(i, " ")

string = string.replace(" ", "")

print(result + len(string))

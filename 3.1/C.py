# FILE C.py
Len = int(input())
N = int(input())

strings = []
for i in range(N):
    strings.append(input())
for string in strings:
    if len(string) > Len:
        print(string[0:Len - 3] + "...")
    else:
        print(string)

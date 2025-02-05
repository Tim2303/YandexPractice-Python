# FILE J.py
N = int(input())

print("А Б В")
for i in range(1, N - 1):
    for j in range(1, N - i):
        k = N - i - j
        print(i, j, k)

# FILE I.py
N = int(input())

res = 0
for i in range(N):
    new_num = input()
    max = 0
    for j in new_num:
        max = max if int(j) < max else int(j)

    res = res * 10 + max
print(res)

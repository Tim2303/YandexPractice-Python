# FILE H.py
N = int(input())

best_name = ""
best_num = 0

for i in range(N):
    name = input()
    number = input()

    summ = 0
    for j in number:
        summ += int(j)

    if summ >= best_num:
        best_name = name
        best_num = summ

print(best_name)

# FILE T.py
N = int(input())
best_num = 0
best_base = 0

for base in range(10, 1, -1):
    summ = 0
    num = N
    while num > 0:
        summ += (num % base)
        num //= base
    if summ >= best_num:
        best_num = summ
        best_base = base

print(best_base)

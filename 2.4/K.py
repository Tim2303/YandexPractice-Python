# FILE K.py
N = int(input())

res_number = 0
for i in range(N):
    n = int(input())
    IsPrime = True

    if n == 1:
        IsPrime = False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                IsPrime = False
                break
    res_number += IsPrime

print(res_number)

# FILE F.py
N = int(input())
gcd = int(input())

for i in range(N - 1):
    number = int(input())
    while number != 0:
        gcd, number = number, gcd % number

print(gcd)

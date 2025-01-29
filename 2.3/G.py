a, b = int(input()), int(input())
n1, n2 = a, b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(int(n1 * n2 / (a + b)))

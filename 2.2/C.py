Petya = int(input())
Vasya = int(input())
Tolya = int(input())

maximal = max(Petya, Vasya, Tolya)

if maximal == Petya:
    print("Петя")
elif maximal == Vasya:
    print("Вася")
else:
    print("Толя")

Petya = int(input())
Vasya = int(input())
Tolya = int(input())

arr = [(Petya, "Петя"), (Vasya, "Вася"), (Tolya, "Толя")]
arr.sort(key=lambda v: v[0])

print("1.", arr[2][1])
print("2.", arr[1][1])
print("3.", arr[0][1])

n1 = int(input())
n2 = int(input())

res = (n1 % 10 + n2 % 10) % 10
n1 = n1 // 10
n2 = n2 // 10

res += ((n1 % 10 + n2 % 10) % 10) * 10
n1 = n1 // 10
n2 = n2 // 10

res += ((n1 % 10 + n2 % 10) % 10) * 100
print(res)

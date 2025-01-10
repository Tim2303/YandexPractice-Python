num = int(input())

n1 = num % 10
n2 = num // 10 % 10
n3 = num // 100 % 10

maxml = max(n1, n2, n3)
minml = min(n1, n2, n3)

if maxml + minml == (n1 + n2 + n3 - maxml - minml) * 2:
    print("YES")
else:
    print("NO")

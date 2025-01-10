n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 ** 2 == n2 ** 2 + n3 ** 2 or n2 ** 2 == n1 ** 2 + n3 ** 2 or n3 ** 2 == n1 ** 2 + n2 ** 2:
    print("100%")
elif n1 ** 2 > n2 ** 2 + n3 ** 2 or n2 ** 2 > n1 ** 2 + n3 ** 2 or n3 ** 2 > n1 ** 2 + n2 ** 2:
    print("велика")
else:
    print("крайне мала")

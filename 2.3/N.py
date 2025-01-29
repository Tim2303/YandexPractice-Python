n = int(input())
IsPrime = True

if n == 1:
    IsPrime = False
else:
    for i in range(2, (n + 1) // 2 + 1):
        if n % i == 0:
            IsPrime = False
            break

if IsPrime:
    print("YES")
else:
    print("NO")

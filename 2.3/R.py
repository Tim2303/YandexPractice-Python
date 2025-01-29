n = int(input())

if n < 2:
    print(n)

div = 1
while n > 1:
    div += 1
    if n % div == 0:
        print(div, end="")
        if n != div:
            print(" * ", end="")
        n //= div
        div = 1

num = int(input())

firstp = num % 10 + num // 10 % 10
secondp = num // 10 % 10 + num // 100

if firstp > secondp:
    print(f"{firstp}{secondp}")
else:
    print(f"{secondp}{firstp}")

# FILE E.py
N = int(input())

sum = 0
for i in range(N):
    isZaika = False
    while (string := input()) != "ВСЁ":
        if string == "зайка":
            isZaika = True
    sum += 1 if isZaika else 0

print(sum)

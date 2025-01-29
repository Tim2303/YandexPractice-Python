n = int(input())
bestn = input()
for i in range(n - 1):
    name = input()
    if name < bestn:
        bestn = name
print(bestn)

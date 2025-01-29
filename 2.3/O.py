n = int(input())
sum = 0
for i in range(n):
    string = input()
    if string.find("зайка") != -1:
        sum += 1
print(sum)

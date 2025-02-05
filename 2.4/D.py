# FILE D.py
N = int(input())
sum = 0

for i in range(N):
    number = input()
    for j in number:
        sum += int(j)
print(sum)

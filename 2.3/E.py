sum = 0
while (prd := float(input())) != 0:
    if (prd >= 500):
        prd *= 0.9
    sum += prd
print(sum)

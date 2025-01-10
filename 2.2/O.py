n1 = int(input())
n2 = int(input())

n11 = n1 // 10
n12 = n1 % 10
n22 = n2 // 10
n21 = n2 % 10

maximal = max(n11, n12, n21, n22)
minimal = min(n11, n12, n21, n22)
mid = n11 + n12 + n21 + n22 - maximal - minimal

print(f"{maximal}{mid % 10}{minimal}")

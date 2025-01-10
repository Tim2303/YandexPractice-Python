num = int(input())

n1 = num % 10
n2 = num // 10 % 10
n3 = num // 100

maxml = max(n1, n2, n3)
minml = min(n1, n2, n3)
midml = n1 + n2 + n3 - maxml - minml

maximal = maxml * 10 + midml

if minml != 0:
    minimal = minml * 10 + midml
elif midml != 0:
    minimal = midml * 10 + minml
else:
    minimal = maxml * 10 + minml

print(minimal, maximal)

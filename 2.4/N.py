# FILE N.py
Height = int(input())
Length = int(input())
indent = len(str(Length * Height))

for i in range(Height):
    for j in range(Length):
        if i % 2 == 0:
            print(f"{1 + i * Length + j:>{indent}}", end=" ")
        else:
            print(f"{(i + 1) * Length - j:>{indent}}", end=" ")
    print()

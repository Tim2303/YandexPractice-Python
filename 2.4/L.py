# FILE L.py
Height = int(input())
Length = int(input())

indent = len(str(Length * Height))

for i in range(Height):
    for j in range(Length):
        print(f"{1 + i * Length + j:>{indent}}", end=" ")
    print()

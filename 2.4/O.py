# FILE O.py
Height = int(input())
Length = int(input())
indent = len(str(Length * Height))

for i in range(Height):
    for j in range(Length):
        if j % 2 == 0:
            print(f"{1 + i + j * Height:>{indent}}", end=' ')
        else:
            print(f"{(j + 1) * Height - i:>{indent}}", end=" ")
    print()

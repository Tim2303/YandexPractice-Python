# FILE M.py
Height = int(input())
Length = int(input())
indent = len(str(Length * Height))

for i in range(Height):
    for j in range(Length):
        print(f"{1 + i + j * Height:>{indent}}", end=' ')
    print()

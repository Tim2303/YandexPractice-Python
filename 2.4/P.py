# FILE P.py
Size = int(input())
Indent = int(input())

for i in range(1, Size + 1):
    for j in range(1, Size + 1):
        print(f"{i * j:^{Indent}}", end='')
        if j != Size:
            print("|", end='')
    print()

    if i != Size:
        print("-" * (Size * Indent + Size - 1))

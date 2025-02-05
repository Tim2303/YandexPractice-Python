# FILE S.py
N = int(input())
Indent = len(str((N + 1) // 2))

for i in range(N):
    for j in range(N):
        print(f"{min(i + 1, j + 1, N - i, N - j):>{Indent}}", end=' ')
    print()

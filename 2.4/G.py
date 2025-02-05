# FILE G.py
N = int(input())

for i in range(N):
    for j in range(i + 3, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i + 1}!!!")

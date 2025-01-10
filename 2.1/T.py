N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

w1 = (M - K2) * N / (K1 - K2)

print(int(w1), int(N - w1))

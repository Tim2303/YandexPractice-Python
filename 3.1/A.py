# FILE A.py
N = int(input())
IsRight = True
for i in range(N):
    string = input()
    if string == string.lower().lstrip("абв"):
        IsRight = False
print("YES" if IsRight else "NO")

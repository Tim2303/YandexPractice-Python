# FILE E.py
string = input()
IsPali = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        IsPali = False
        break
print("YES" if IsPali else "NO")

n = int(input())

string = str(n)
leng = len(str(n))
rlen = leng // 2

isPalindrome = True
for i in range(rlen):
    if string[i] != string[leng - 1 - i]:
        isPalindrome = False
print(("YES" if isPalindrome else "NO"))

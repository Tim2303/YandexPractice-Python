string1 = input()
string2 = input()
string3 = input()

res = ""

if "зайка" in string1:
    res = string1
if "зайка" in string2 and (res == "" or res > string2):
    res = string2
if "зайка" in string3 and (res == "" or res > string3):
    res = string3
print(res, len(res))

# FILE D.py
strings = []
while (string := input()) != "":
    strings.append(string)
for string in strings:
    if string[-3:] != "@@@":
        if string[0:2] == "##":
            string = string[2:]
        print(string)

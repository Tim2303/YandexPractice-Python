counter = 0
while (txt := input()) != "Приехали!":
    if txt.find("зайка") != -1:
        counter += 1
    else:
        pass
print(counter)

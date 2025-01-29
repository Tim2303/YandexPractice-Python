step = 250
num = 500

print(num)
while (string := input()) != "Угадал!":
    match string:
        case "Меньше":
            num -= step
        case "Больше":
            num += step
    step = (step + 1) // 2
    print(num)
print("Число отгадано")

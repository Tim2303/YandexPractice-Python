x, y = 0, 0
while (dest := input()) != "СТОП":
    match dest:
        case "ВОСТОК":
            x += int(input())
        case "ЗАПАД":
            x -= int(input())
        case "СЕВЕР":
            y += int(input())
        case "ЮГ":
            y -= int(input())

print(f"{y}\n{x}")
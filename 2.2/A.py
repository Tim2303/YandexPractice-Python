print("Как Вас зовут?")
name = input()
print("Здравствуйте, " + name + "!")

print("Как дела?")
ans = input()
match ans:
    case "хорошо": print("Я за вас рада!")
    case "плохо": print("Всё наладится!")

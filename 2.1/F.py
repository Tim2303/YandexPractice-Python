name = input()
cost = int(input())
weight = int(input())
money = int(input())

print(f"Чек\n{name} - {weight}кг - {cost}руб/кг")
print(f"Итого: {weight * cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - weight * cost}руб")

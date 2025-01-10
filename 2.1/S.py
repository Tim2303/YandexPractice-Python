name = input()
price = int(input())
weight = int(input())
cash = int(input())

price_str = str(weight) + "кг * " + str(price) + "руб/кг"

print("================Чек================")
print(f"Товар:{name: >29}")
print(f"Цена:{price_str: >30}")
print(f"Итого:{weight * price: >26}" + "руб")
print(f"Внесено:{cash: >24}" + "руб")
print(f"Сдача:{cash - weight * price: >26}" + "руб")
print("===================================")

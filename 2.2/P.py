pv = int(input())
vv = int(input())
tv = int(input())

places = [(pv, "Петя"), (vv, "Вася"), (tv, "Толя")]
places.sort()

place1 = "        " + str(f"{places[2][1]: ^8}")
place2 = str(f"{places[1][1]: ^8}")
place3 = "                " + str(f"{places[0][1]: ^8}")

print(place1)
print(place2)
print(place3)
print("   II      I      III")


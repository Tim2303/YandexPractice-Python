hours = int(input())
minutes = int(input())
delta = int(input())

plush = (minutes + delta) // 60
print(f"{(hours + plush) % 24:0>2}" + ":" + f"{minutes + delta - plush * 60:0>2}")

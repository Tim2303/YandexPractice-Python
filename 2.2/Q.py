a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if a == b == c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    print(f"{-(c / b):.2f}")
elif a == b == 0:
    print("No solution")
elif a == c == 0:
    print(0)
elif D < 0:
    print("No solution")
elif D == 0:
    print(f"{(-b) / 2 * a:.2f}")
else:
    n1 = (-b - D ** 0.5) / (2 * a)
    n2 = (-b + D ** 0.5) / (2 * a)
    print(f"{min(n1, n2):.2f}", f"{max(n1, n2):.2f}")


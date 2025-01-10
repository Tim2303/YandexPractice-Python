N = int(input())
M = int(input())

p = 6 + N
v = 9 + M

match p > v:
    case 1: print("Петя")
    case 0: print("Вася")

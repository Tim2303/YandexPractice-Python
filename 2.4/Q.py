# FILE Q.py
N = int(input())

poly_num = 0
for i in range(N):
    num_str = input()
    str_len = len(num_str)

    is_poly = True
    for j in range(str_len // 2):
        if num_str[j] != num_str[str_len - j - 1]:
            is_poly = False
            break
    poly_num += is_poly

print(poly_num)

# FILE C.py
n = int(input())
cnt = 1
flag = True
row_num = 1

while flag:
    for i in range(row_num):
        print(cnt, end=' ')
        cnt += 1
        if cnt > n:
            flag = False
            break
    print()
    row_num += 1

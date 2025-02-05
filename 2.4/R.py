# FILE R.py
N = int(input())

cnt = 0
Width = 1
max_length = 0

while cnt <= N:
    string_length = 0
    for position in range(Width):
        cnt += 1
        if cnt <= N:
            string_length += len(str(cnt))
        if position < Width - 1 and cnt < N:
            string_length += 1

    if max_length < string_length:
        max_length = string_length
    Width += 1

cnt = 0
Width = 1

while cnt <= N:
    string = ''
    for position in range(Width):
        cnt += 1
        if cnt <= N:
            string += str(cnt)
        if position < Width - 1 and cnt < N:
            string += ' '
    Width += 1
    print(f'{string:^{max_length}}')

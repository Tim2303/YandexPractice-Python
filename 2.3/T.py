n = int(input())
h0 = 0
err_line = 0
is_err = False

for i in range(n):
    block = int(input())
    hi = block % 256
    ri = (block // 256) % 256
    mi = block // 256 ** 2
    new_h = (37 * (mi + ri + h0)) % 256

    if new_h != hi or new_h >= 100:
        is_err = True
        err_line = i
        break

    h0 = new_h

if is_err:
    print(err_line)
else:
    print(-1)

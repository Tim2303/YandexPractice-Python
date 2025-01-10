elf = int(input())
gnm = int(input())
lud = int(input())

if elf % 10 == gnm % 10 == lud % 10:
    print(int(elf % 10))
elif elf // 10 == gnm // 10 == lud // 10:
    print(int(elf // 10))
else:
    print(" ")

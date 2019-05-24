#Power of Four
num = int(input("nhap so"))

def powerOf4(num):
    n = 1
    while(n<num):
        n *= 4
    if n != num:
        return False
    else:
        return True

print(powerOf4(num))
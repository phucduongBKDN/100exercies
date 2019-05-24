#Valid Perfect Square
num = int(input("nhap so"))

def validPerfectSpare(num):
    for i in range(int(num/2)):
        if num == i*i:
            return True
    return False

print(validPerfectSpare(num))

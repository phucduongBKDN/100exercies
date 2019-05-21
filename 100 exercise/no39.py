#Add Digits
num = 38

def addDigits(num):
    lenght = len(str(num))
    if lenght == 1:
        return num
    else:
        sum = 0
        for i in str(num):
            sum = sum + int(i)
        return addDigits(sum)

print(addDigits(num))

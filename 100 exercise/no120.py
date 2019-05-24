#Ugly Number
num = 6

def uglyNumber(num):
    if num <= 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num = num / i
    if num == 1:
        return True
    else:
        return False

print(uglyNumber(num))


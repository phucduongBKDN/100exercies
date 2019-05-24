#Happy Number
number = 19
def split(number):
    return [int(i) for i in str(number)]
def happyNumber(number):
    while(1):
        list = split(number)
        sum = 0
        for i in list:
            sum += i*i
        if sum == 1:
            return True
        else:
            number = sum
            happyNumber(number)

print(happyNumber(number))
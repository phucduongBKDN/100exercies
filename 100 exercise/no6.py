#Self Dividing Numbers
lower  = int(input("enter lower number "))
upper  = int(input("enter upper number "))
def split(word):
    return [char for char in word]


def isSelfDividing(n):
    origin = n
    while (n > 0):
        try:
            digit = n % 10
            if (origin % digit != 0):
                return False
            n = n // 10
        except ZeroDivisionError:
            return False
    return True

listnumber = []
for i in range(lower,upper +1):
    if (isSelfDividing(i)):
        listnumber.append(i)

print(listnumber)




# Number Complement

def split(word):
    return [char for char in word]
num = int(input("Enter num: "))
def numberComplement(num):
    num= format(num,'b')
    # print(type(num))
    list = split(num)
    list2 = []
    print(list)
    for i in list:
        i = int(i)
        i ^= 1
        i = str(i)
        list2.append(i)
    list2 = ''.join(list2)
    number = int(list2, 2)
    return number

print(numberComplement(num))



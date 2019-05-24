#Reverse Integer
input = 1230
def split(word):
    return [char for char in word]

def reverseInterger(input):
    list = split(str(input))
    list.reverse()
    if int(list[0]) == 0:
        del list[0]
    list = int(''.join(list))
    return list

print(reverseInterger(input))



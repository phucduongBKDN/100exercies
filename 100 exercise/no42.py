#Move Zeroes
input = [0,1,0,3,12]

def moveZerose(list):
    for i in range(len(list)):
        if list[i] == 0:
            list.append(0)
            del list[i]
    return (list)

print(moveZerose(input))
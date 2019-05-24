#Squares of a Sorted Array
input = [-4,-1,0,3,10]

def squares(input):
    list = []
    for i in input:
        list.append(i*i)
    list.sort()
    return list

print(squares(input))
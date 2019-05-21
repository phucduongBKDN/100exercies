#Find All Numbers Disappeared in an Array
input = [4,3,2,7,8,2,3,1]
def numDis(array):
    save = []
    for i in range(1,len(array)+1):
        if not i in array:
            save.append(i)
    return save

print(numDis(input))

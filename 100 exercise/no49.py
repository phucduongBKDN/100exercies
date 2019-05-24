#Monotonic Array
input = [1,2,2,3]

def monotonic(list):
    if list[0]>list[1]:
        for i in range(1,len(list)-1):
            if list[i]<list[i+1]:
                return False
    if list[0]<list[1]:
        for i in range(1, len(list)-1):
            if list[i] > list[i + 1]:
                return False
    return True

print(monotonic(input))





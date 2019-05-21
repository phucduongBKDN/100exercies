#Single Number
list =[4,1,2,1,2]

def singleNumber(nums):
    check = 0
    for i in list:
        check ^= i
        print(check)
    return check
singleNumber(list)
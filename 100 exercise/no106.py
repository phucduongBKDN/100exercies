#Remove Element
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
def removeElement(nums,val):
    i = 0
    while(i<len(nums)):
        print('i:',i)
        if nums[i] == val:
            del nums[i]
            i -= 1
        i += 1

    return nums

print(removeElement(nums,val))
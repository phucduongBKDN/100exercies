#Two Sum
nums = [2, 7, 11, 15]
target = 9

def twoSum(nums,target):
    list = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                list.append(i)
                list.append(j)
    return list

print(twoSum(nums,target))
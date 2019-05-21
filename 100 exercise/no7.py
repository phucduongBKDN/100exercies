#Array Partition I
nums = [1,7,6,8,9,10,20,46]

def arrayPartition(nums):
    return sum(sorted(nums)[::2])

print(arrayPartition(nums))


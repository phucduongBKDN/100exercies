#Two Sum IV - Input is a BST
input = [5,3,6,2,4,0,7] #tree
target = 9
def twoSum(input,target):
    for i in range(len(input)):
        sub = 0
        sub = target - input[i]
        if sub in input:
            return True
    return False

print(twoSum(input,target))

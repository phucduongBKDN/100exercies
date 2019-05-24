#Minimum Moves to Equal Array Elements

input = [1,2,3]
def minMoves(nums):
    return sum(nums) - min(nums) * len(nums)

print(minMoves(input))

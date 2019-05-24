#Maximum Subarray

input = [-2,1,-3,4,-1,2,1,-5,4]

def maximumSubarray(input):
    save = 0
    for i in range(len(input)-1):
        sum = input[i]
        if save < sum:
            save = sum
        for j in range(i+1,len(input)):
            sum += input[j]
            if save < sum:
                save = sum
    return save

print(maximumSubarray(input))

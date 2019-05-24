#Find Pivot Index
input = [1, 7, 3, 6, 5, 6]

def findPivot(input):
    for i in range(1,len(input)-1):
        sum1 = 0
        sum2 = 0
        for j in range(i):
            sum1 += input[j]
        for k in range(i+1,len(input)):
            sum2 += input[k]
        if sum1 == sum2:
            return i

print(findPivot(input))
#House Robber
input = [2,7,9,3,1]

def houserRobber(input):
    sum1 = 0
    sum2 = 0
    for i in range(0,len(input),2):
        sum1 += input[i]
    for j in range(1,len(input),2):
        sum2 += input[i]
    if sum1 > sum2:
        return sum1
    else:
        return sum2

print(houserRobber(input))

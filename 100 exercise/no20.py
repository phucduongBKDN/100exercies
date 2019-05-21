#Reshape the Matrix

def matrixReshape(nums, r, c):
    l = []
    for i in nums:
        for j in range(len(i)):
            l.append(i[j])
    if r * c != len(l):
        return nums
    k = []
    for i in range(int(len(l) / c)):
        k.append(l[i * c:(i + 1) * c])
    return k

matrix = [[1,6],
        [3,4],
        [5,7]]
r = 2
c = 3

print(matrixReshape(matrix,r,c))
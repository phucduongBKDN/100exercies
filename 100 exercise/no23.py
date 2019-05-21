#Transpose Matrix

input =[[1,2,3],  #0,1
        [4,5,6],       #1,0
        [7,8,9]]

def swap(a,b):
    c =a
    a=b
    b=c
    return a ,b


def transposeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = swap(matrix[i][j],matrix[j][i])
    return matrix

print(transposeMatrix(input))



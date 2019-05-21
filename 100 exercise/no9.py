

N = 3
M = 4

def checkDiagonal(mat, i, j):
    res = mat[i][j]
    i += 1
    j += 1
    while (i < N and j < M):
        if (mat[i][j] != res):
            return False
        i += 1
        j += 1
    return True

def isToeplitz(mat):
    for j in range(M):
        if not (checkDiagonal(mat, 0, j)):
            return False
    for i in range(1, N):
        if not (checkDiagonal(mat, i, 0)):
            return False
    return True

mat = [[1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]]

if (isToeplitz(mat)):
    print("true")
else:
    print("false")
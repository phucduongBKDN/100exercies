#Flipping an Image

mat = [[1,1,0],[1,0,1],[0,0,0]]
def flipAndInvertImage(mat):
    rows = len(mat)
    cols = len(mat[0])
    for row in range(rows):
        mat[row] = mat[row][::-1]
        for col in range(cols):
            mat[row][col] ^= 1
    return mat
print(flipAndInvertImage(mat))

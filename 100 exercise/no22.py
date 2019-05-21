#Island Perimeter
input = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]



def islandPerimeter(matrix):
    perimeter = 0
    index = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('index',index)
            if matrix[i][j] == 1:
                perimeter = perimeter + 4
                print('perimeter ban dau:',perimeter)
                try:
                    if (matrix[i][j+1] == 1):
                        perimeter = perimeter -2
                        print('if1')
                except:
                    pass
                try:
                    if (matrix[i+1][j] == 1):
                        perimeter = perimeter -2
                        print('if2')
                        print('perimeter2',perimeter)
                except:
                    pass
            index=index+1
    return perimeter

print(islandPerimeter(input))




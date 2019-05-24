#Pascal's Triangle II
input = 3

def solution(rowIndex):
    res = [1] + [0] * rowIndex
    for i in range(rowIndex):
        res[0] = 1
        for j in range(i+1, 0, -1):
            res[j] = res[j] + res[j-1]
    return res

print(solution(input))

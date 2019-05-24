#Range Addition II

m = 3
n = 3
operations = [[2,2],[3,3]]

def maxCount(m, n, ops):
    if not ops:
        return m * n
    return min([op[0] for op in ops]) * min([op[1] for op in ops])

print(maxCount(m,n,operations))
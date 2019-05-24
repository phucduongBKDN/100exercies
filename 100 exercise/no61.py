#Same Tree
tree1 = [1,2]
tree2 = [1,0,2]

def sameTree(a,b):
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]:
            return  False
    return True

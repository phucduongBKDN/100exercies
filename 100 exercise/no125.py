#Range Sum of BST
root = [10,5,15,3,7,0,18]
L = 7
R = 15
def rangeSumofBST(root,l,r):
    sum = 0
    for i in range(len(root)):
        if l <= root[i] <= r:
            sum += root[i]
    return sum
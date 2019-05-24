#Minimum Absolute Difference in BST
tree = [1,2,3,5,6,4]
def solution(tree):
    tree.sort()
    memo = tree[1] - tree[0]
    for i in range(2,len(tree)-1):
        if memo > (tree[i+1]-tree[i]):
            memo = tree[i+1]-tree[i]
    return memo

print(solution(tree))
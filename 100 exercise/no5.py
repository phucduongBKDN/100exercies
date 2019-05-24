#merge bts
tree1 = [1,3,2,5]
tree2 = [2,1,3,0,4,0,7]

def mergebts(tree1,tree2):
    tree =[]
    for i in range(min(len(tree1),len(tree2))):
        tree.append(tree1[i]+tree2[i])
    for i in range( min(len(tree1),len(tree2)), max(len(tree1),len(tree2)) ):
        tree.append(tree2[i])
    return tree

print(mergebts(tree1,tree2))
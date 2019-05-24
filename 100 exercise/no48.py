#Convert BST to Greater Tree
input = [5,2,13]

def greaterTree(tree):
    output = []
    for i in range(len(tree)):
        sum = tree[i]
        for j in range(len(tree)):
            if i == j:
                continue
            else:
                if tree[j]>tree[i]:
                    sum += tree[j]
        output.append(sum)
    return output

print(greaterTree(input))

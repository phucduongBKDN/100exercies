#Sum of Left Leaves
tree = [3,9,20,0,0,15,7]

def sumleft(tree):
    tem = 0
    sum = 0
    for i in range(len(tree)):
        if i == 0:
            continue
        else:
            if tem == 0:
                tem ^=1
                continue
            else:
                sum += tree[i]
                tem ^= 1
    return sum

print(sumleft(tree))

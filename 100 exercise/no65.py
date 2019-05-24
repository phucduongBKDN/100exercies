#Binary Tree Tilt

tree = [1,2,3,0,2,1,4]

def btt(tree):
    sum  = 0
    for i in range(1,len(tree),2):
        sum += abs(tree[i]-tree[i+1])
    return sum

print(btt(tree))
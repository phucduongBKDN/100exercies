#Maximum Depth of Binary Tree
binarytree = [3,9,20,0,0,15,7]

lenght = len(binarytree)
count = 0
a = 2
while(lenght>1):
    lenght = lenght - a
    a = a*2
    count= count +1
count = count+1
print(count)


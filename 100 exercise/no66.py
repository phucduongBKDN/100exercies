#Delete Node in a Linked List
head = [4,5,1,9]
node = 5

for i in range(len(head)-1):
    if head[i] == node:
        del head[i]
print(head)
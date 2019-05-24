# Search Insert Position
list = [1,3,5,6]
k = 5
def searchInPo(list,k):
    if list.index(k):
        return list.index(k)
    else:
        for i in range(len(list)):
            if list[i] > k:
                return i

print(searchInPo(list,k))
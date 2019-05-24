#Contains Duplicate
input = [1,1,1,3,3,4,3,2,4,2]

def constainDup(input):
    set = set(input)
    if (set==input):
        return False
    else:
        return True


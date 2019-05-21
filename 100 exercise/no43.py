#Find the Difference
s = "abcdre"
t = "abrecde"

def split(word):
    return [char for char in word]

def findDifference(s, t):
    lists = split(s)
    listt = split(t)
    lists.sort()
    listt.sort()
    print(lists)
    print(listt)
    for i in range(len(lists)):
        if lists[i] != listt[i]:
            return listt[i]


print(findDifference(s,t))
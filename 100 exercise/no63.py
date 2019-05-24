#First Unique Character in a String
import collections

s = "loveleetcode"



def solution(s):
    d = collections.Counter(s)
    print(d)
    count = 0
    index = 0
    for i in d.values():
        if i == 1:
            return index
        index +=1

print(solution(s))
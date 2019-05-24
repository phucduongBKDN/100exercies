#Set Mismatch
import collections
input = [1,2,2,4]

def setMismatch(input):
    dict = collections.Counter(input)
    listn = []
    output = []
    for i in dict:
        if dict[i] > 1:
            double = i
    output.append(i)
    for i in range(1,len(input)+1):
        listn.append(i)
    missing = list(set(listn) - set(input))
    output = output + missing
    return output


print(setMismatch(input))

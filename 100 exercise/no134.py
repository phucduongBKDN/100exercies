#String Compression
import collections

input = ["a","a","b","b","c","c","c"]

def stringCompression(input):
    collection = collections.Counter(input)
    list = []
    for i in collection:
        list.append(i)
        list.append(collection[i])
    return list

print(stringCompression(input))
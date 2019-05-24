#Find Mode in Binary Search Tree
import collections
from collections import Counter
tree = [1,0,2,2]
for i in collections.Counter(tree):
    max = 0
    if collections.Counter(tree)[i] > max:
        max = collections.Counter(tree)[i]
print(max)



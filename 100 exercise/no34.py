# Uncommon Words from Two Sentences
import collections
a = input("Enter a: ")
b = input("Enter b: ")

def uncommonWords(A, B):
    count = collections.Counter(A.split()) #generate tuple
    count += collections.Counter(B.split())
    return [word for word in count if count[word] == 1]

print(uncommonWords(a,b))
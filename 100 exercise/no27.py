#Longest Uncommon Subsequence I

def lus(a, b):
    return max(len(a), len(b)) if a != b else -1
a = "aba"
b = "cdc"
print(lus(a,b))



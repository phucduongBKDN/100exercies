#Detect Capital

def detectCapital(strA):
    if strA.isupper():
        return True
    elif strA.islower():
        return True
    elif( 65 <= ord(strA[0]) <= 90):
        if strA[1:].islower():
            return True
    return False

stringA = "USA"
print(detectCapital(stringA))
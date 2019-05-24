#Ransom Note
def split(word):
    return [char for char in word]

def ransomNote(a,b):
    lista = set(split(a))
    listb = set(split(b))
    check = False
    if all(x in listb for x in lista):
        check = True
    return check

a = "aa"
b = "aab"
print(ransomNote(a,b))


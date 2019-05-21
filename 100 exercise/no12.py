#Reverse Words in a String III

j = input("Enter string: ")
def reverseWords(s):
    l = s.split()
    k = []
    for i in l:
        k.append(i[::-1])
    t = ' '.join(k)
    return t

print(reverseWords(j))
#Jewels and stones

j = input("Enter Jewels: ")
j = ''.join(set(j))
print('Jewels:',j)
s = input("Enter Stones: ")
print('Stones',s)

def split(word):
    return [char for char in word]

listJ = split(j)
count = 0

for je in listJ:
    count = count + s.count(je)
print(count)







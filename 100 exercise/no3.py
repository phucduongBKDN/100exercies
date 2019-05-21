#Hamming Distance

num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))
print(format(num1,"b"))
print(format(num2,"b"))
num1 = format(num1,"b")
num2 = format(num2,"b")
def split(word):
    return [char for char in word]

num1 = split(str(num1))
num2 = split(str(num2))
print(num1)
print(num2)
count = 0
for i in range (min(len(num1),len(num2))):
    if (num1[i]!=num2[i]):
        count = count +1
print(count)
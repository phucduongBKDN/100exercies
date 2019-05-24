#Reverse Only Letters
input = "a-bC-dEf-ghIj"

def split(word):
    return [char for char in word]

def reverse(input):
    list = []
    input = split(input)
    for i in range(len(input)):
        if input[i].isalpha():
            list.append(input[i])
    for i in range(len(input)):
        if input[i].isalpha():
            input[i] = list.pop()
    str = ''.join(input)
    return str

print(reverse(input))
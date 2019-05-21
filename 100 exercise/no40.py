#Count Binary Substrings
input = "00110011"

def split(word):
    return [char for char in word]


def cbs(input):
    list = split(input)

    count = 0
    lenght = len(list)

    for i in range(lenght):
        c0 = 0
        c1 = 0
        print('i',list[i])
        if list[i] == "0":
            c0 = 1
        else:
            c1 = 1
        for j in range(i+1, len(list)):
            print('j',list[j])
            if list[j] == "0":
                c0 = c0 +1
            else:
                c1 = c1 +1
            if c0 == c1:
                count = count +1
                break
    return count


print(cbs(input))
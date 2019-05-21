# Baseball Game
input = ["5","2","C","D","+"]
add = []
output = 0
index = 0
for i in input:
    if (i == 'C'):
        input.pop(index)
        input.pop(index-1)
        # print(input)
        index = index - 2
    index = index+1

# print(input)
for j in input:
    if (j == 'D'):
        output = output + int(add[-1])*2
        add.append(int(add[-1])*2)
        # print('D',output)
    elif (j == '+'):
        output = output + int(add[-1]) + int(add[-2])
        # print('add[-1]:',add[-1])
        # print('add[-2]:', add[-2])
        # print('+',output)
    else:
        output = output + int(j)
        add.append(j)
        # print('num',output)

print(output)





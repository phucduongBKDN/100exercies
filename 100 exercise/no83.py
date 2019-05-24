#Missing Number
input = [9,6,4,2,3,5,7,0,1]

check = 0
max = max(input)
for i in range(1,max):
    if not i in set(input):
        check = i

print(i)
#Majority Element
input = [2,2,1,1,1,2,2]
thisdict = {}
set = set(input)
for i in set:
    thisdict[str(i)] = input.count(i)
max = 0
for i in set:
    if thisdict[str(i)] > max:
        max = thisdict[str(i)]
        output = i
print(output)
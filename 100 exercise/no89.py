#Largest Number At Least Twice of Others
input = [3, 6, 1, 0]
max = max(input)
index = input.index(max)
for i in input:
    if i ==max:
        continue
    if (i*2)>max:
        index = -1
print(index)


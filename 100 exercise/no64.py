#Two Sum II - Input array is sorted
list =  [2,7,11,15]
target = 9
index = []
for i in range(len(list)):
    if list[i] >= target:
        break
    memo = target - list[i]
    for j in range(i+1,len(list)):
        if list[j] == memo:
            index.append(i+1)
            index.append(j+1)

print(index)

# Longest Harmonious Subsequence

input = [1,3,2,2,5,2,3,7]

set = set(input)
set = list(set)
print(set)
output = 0
count = 0
for i in range(len(set)-1):
    if set[i+1]-set[i] == 1:
        #count
        count = input.count(set[i])+ input.count(set[i+1])
        if count > output:
            output = count
print(output)

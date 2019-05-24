#Longest Continuous Increasing Subsequence
input = [1,3,5,4,7]
count = 1
save = 0
for i in range(len(input)-1):
    if input[i]<input[i+1]:
        count += 1
        if count > save:
            save = count
    else:
        count = 1

if save == 0:
    save+=1

print(save)


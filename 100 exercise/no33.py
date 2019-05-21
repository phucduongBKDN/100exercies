# Max Consecutive Ones
input =  [1,1,0,1,1,1]
count = 0
for i in input:
    if i==1:
        count = count+1
    else:
        count = 0
print(count)
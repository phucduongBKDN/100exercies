#Maximum Average Subarray I
input = [1,12,-5,-6,50,3]
k = 4

def mas(input,k):
    save = 0
    for i in range(len(input)-k):
        sum = input[i]
        for j in range(1,k+1):
            sum += input[i+j]
        if sum > save:
            save = sum
    return save/k

print(mas(input,k))


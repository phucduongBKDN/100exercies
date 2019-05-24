#Plus One

input = [4,3,2,2]
num = [9,9,9]

def plusOne(num):
        num[len(num)-1] += 1
        index = len(num) - 1
        while(True):
            if num[0] == 10:
                num[0]=0
                num.insert(0,1)
                break
            if num[index] == 10:
                num[index] = 0
                num[index-1] += 1
                index -= 1
            else:
                break
        return num

print(plusOne(num))


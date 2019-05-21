#Peak Index in a Mountain Array

def peakIndexInMountainArray(self, A):
    if len(A) == 1: return 0  # 设置递归出口

    if len(A) == 2:
        if A[0] > A[1]: return 0
        return 1

    mid = len(A) // 2

    if A[mid - 1] > A[mid]:  # 左递归
        num = self.peakIndexInMountainArray(A[0:mid])
        return num
    elif A[mid + 1] > A[mid]:  # 右递归
        num = self.peakIndexInMountainArray(A[mid + 1:])
        return num + 1 + mid
    else:  # 其他情况
        return mid



input = [0,2,1,0]
check = 1
for i in range(1,len(input)-1):
    for j in range(len(input)):
        if i == j:
            continue
        print('i:',i)
        print('j:', j)
        print('input[i]',input[i])
        print('input[j]', input[j])

        if input[j]>input[i]:
            check = 0
            print('check:',check)
    if check == 1:
        break


if check:
    print("A is mountain")
else:
    print("A is not mountain")

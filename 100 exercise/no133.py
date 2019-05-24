#Factorial Trailing Zeroes
num = int(input("nhap so: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def dtz(num):
    n = factorial(num)
    res = [int(x) for x in str(n)]
    count = 0
    for i in range(len(res)):
        if res[i] == 0:
            count += 1
    return count

print(dtz(num))
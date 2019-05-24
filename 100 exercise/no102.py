# Power of Three

n = int(input("Enter n: "))
def powerOfTwo(n):
    check = 3
    if n == 1 or n==3 :
        return True
    while(check<n):
        check *= 3
        if check == n:
            return True
        if check > n:
            return False
print(powerOfTwo(n))
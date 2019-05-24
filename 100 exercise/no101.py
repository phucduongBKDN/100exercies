#Power of Two
n = int(input("Enter n: "))
def powerOfTwo(n):
    check = 2
    if n == 1 or n==2 :
        return True
    while(check<n):
        check *= 2
        if check == n:
            return True
        if check > n:
            return False
print(powerOfTwo(n))
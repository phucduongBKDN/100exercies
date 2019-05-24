#Arranging Coins

num = int(input("nhap so: "))

def arrangingCoins(num):
    count = 1
    while(1):
        num = num - count
        if num < 0:
            count -= 1
            break
        elif num == 0:
            break
        else:
            count += 1
    return count

print(arrangingCoins(num))
# Distribute Candies

def distributeCandies(candies):
    max1 = len(candies) // 2
    max2 = len(set(candies))
    print('set candies:',set(candies))
    return max1 if max1 < max2 else max2


print(distributeCandies([1,100,1,100,1,100]))
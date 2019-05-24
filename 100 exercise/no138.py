#Guess Number Higher or Lower

def guess(mid):
    pass

def guessNumber(self, n):
    left, right = 1, n
    while True:
        mid = (left + right) / 2
        if guess(mid) == 1:
            left = mid + 1
        elif guess(mid) == -1:
            right = mid - 1
        else:
            return mid



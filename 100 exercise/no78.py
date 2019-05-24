#Find Smallest Letter Greater Than Target
letters = ["c", "f", "j"]
target = "a"

def nextGreatestLetter(letters, target):
    for letter in letters:
        if ord(letter) > ord(target):
            return letter
    return letters[0]

print(nextGreatestLetter(letters,target))


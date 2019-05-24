# 1-bit and 2-bit Characters
input = [1, 1, 1, 0]
def isOneBitCharacter(input):
    index = 0
    while index < len(input) - 1:
        index += 2 if input[index] == 1 else 1
    return index == len(input) - 1

print(isOneBitCharacter(input))

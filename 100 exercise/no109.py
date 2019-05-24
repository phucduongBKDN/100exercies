#Number of 1 Bits
input = "00000000000000000000000000001011"
def split(str):
    return [char for char in str]

def numberOf1Bit(input):
    input = split(input)
    count = 0
    for i in input:
        if int(i) == 0:
            count += 1
    return count


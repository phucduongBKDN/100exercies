#Palindrome Number
input = 12321
def reverse(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def palindromeNumber(input):
    str = str(input)
    if str == reverse(str):
        return True
    else:
        return False


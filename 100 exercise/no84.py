# Student Attendance Record I

def split(word):
    return [char for char in word]

input = 'PPALLP'

def solution(input):
    input = split(input)
    countA = 0
    countL = 0
    for i in range(len(input)):
        if input[i] == 'A':
            countA += 1
            if countA > 1:
                return False
        if (input[i] == 'L' and input[i+1] == 'L' and input[i+2] == 'L'):
            return False
    return True

print(solution(input))
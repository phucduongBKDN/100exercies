# Repeated Substring Pattern
input = "abcabcabcabc"

def solution(input):
    return input in input[1:] + input[:-1]

print(solution(input))


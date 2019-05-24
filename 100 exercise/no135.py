#Number of Segments in a String
input = "Hello, my name is John"
def solution(string):
    li = list(string.split(" "))
    return len(li)

print(solution(input))


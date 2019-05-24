#Sort Array By Parity
input = [3,1,2,4]

def solution(list):
    list2 = []
    for i in list:
        if i%2==0:
            list2 = [i] + list2
        if i%2 != 0:
            list2 = [i] + list2
    return list2

print(solution(input))

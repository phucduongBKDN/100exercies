#Construct the Rectangle
import math

input = 12

def rectangleConstruct(input):
    w = int(math.sqrt(input))
    l = int(input / w)
    list = []
    list.append(w)
    list.append(l)
    print(list)

rectangleConstruct(input)
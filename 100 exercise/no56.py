#Best Time to Buy and Sell Stock II
input = [7,1,5,3,6,4]

def stock(input):
    profit = 0
    for i in range(len(input)-1):
        if input[i]>input[i+1]:
            continue
        else:
            profit += input[i+1] - input[i]
            i +=2
    print(profit)

stock(input)


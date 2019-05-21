#Binary Number with Alternating Bits
number = int(input("Enter number: "))
def solution(num):
    bin_n = bin(num)[2:]
    return all(int(bin_n[i]) + int(bin_n[i + 1]) == 1 for i in range(len(bin_n) - 1))

if solution(number):
    print("true")
else:
    print("false")
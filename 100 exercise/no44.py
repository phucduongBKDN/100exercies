#Sum of Two Integers

a = 1
b = 2

def sumOf2Int(a,b):
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= MAX else ~(a ^ mask)

print(sumOf2Int(a,b))



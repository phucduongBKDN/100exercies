# Fizz Buzz
input = int(input("Enter number: "))
output = []
for i in range(1,input+1):
    if(i%3==0 and i%5==0):
        output.append('FizzBuzz')
    elif(i%3==0):
        output.append('Fizz')
    elif(i%5==0):
        output.append('Buzz')
    else:
        output.append(str(i))

print(output)

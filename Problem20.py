import math

#Problem 20

num = 100 #number whose factorial we want to sum
factrl = math.factorial(num)
strFactrl = str(factrl)
total = 0

print('Find the sum of digits in:', strFactrl)

stringTotal = 0

for digit in strFactrl:
    total += int(digit)

print('The sum is', total)



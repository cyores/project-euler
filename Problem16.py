import math

#Problem 16

exp = 1000
power = int(math.pow(2, exp))
strPower = str(power)
total = 0

print('Find the sum of digits in:', strPower)

stringTotal = 0

for digit in strPower:
    total += float(digit)

print('The sum is', total)



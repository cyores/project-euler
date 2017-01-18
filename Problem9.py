import math

# Problem 9

for a in range(1, 333):
    for b in range(2, 499):
        aSbS = (a * a) + (b * b)
        c = math.sqrt(aSbS)
        if a + b + c == 1000:
            print('ANS:', a * b * c)

# a and b cannot be greater or less than the ranges in their respective for loops because
# a < b < c

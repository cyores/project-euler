# Problem 4: Palindromes


def skip(x, y):
    prod = x * y
    if prod % 10 == 0 or prod < largest or prod % 11 != 0 or prod in checked:  # see below for explanation
        return True
    else:
        checked.append(prod)
        return False


def isPalin(n):
    sn = str(n)
    end = len(sn) - 1
    flip = ''
    while end > -1:
        flip += sn[end]
        end -= 1
    if flip == sn:
        return True
    else:
        return False


prod = 0
largest = 0
checked = []  # set containing the product of i and j so we don't check things twice
a = 0
b = 0

for i in range(101, 1000):
    for j in range(101, 1000):
        if skip(i, j):
            continue
        else:
            prod = i * j
        if isPalin(prod) and prod > largest:
            largest = prod
            a = i
            b = j

print('The largest palidrom is', a, '*', b, '=', largest)

# runs in about 21 seconds without the % 11 trick, ans 906609
# runs in about 02 seconds with the % 11 trick, ans 906609

# xy0 * abc wont make any palindromes, so a prod % 10 == 0 wont make any palindromes

# The palindrome can be written as:
#
# abccba
#
# Which then simplifies to:
#
# 100000a + 10000b + 1000c + 100c + 10b + a
#
# And then:
#
# 100001a + 10010b + 1100c
#
# Factoring out 11, you get:
#
# 11(9091a + 910b + 100c)
#
# So the palindrome must be divisible by 11.
# Seeing as 11 is prime, at least one of the numbers must be divisible by 11.
# So brute force in Python, only with less numbers to be checked:

pwr = 5
total = 0
# so we don't have to recalculate powers
powers = {0: 0, 1: 1, 2: 32, 3: 243, 4: 1024, 5: 3125, 6: 7776, 7: 16807, 8: 32768, 9: 59049}

for i in range(2, 999999):
    sum = 0
    istr = str(i)
    for digit in istr:
        x = int(digit)
        sum += powers[x]

    if sum == i:
        print(i)
        total += i

print("Total is ", total)


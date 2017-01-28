# find prime numbers with Eratosthenes Sieve up to 10,000,000 which should be enough
n = 10000000
primes = {1: False}
for i in range(2, n):
    primes[i] = True

for i in range(2, n):
    if primes[i]:
        j = i + i
        while j < n:
            primes[j] = False
            j += i

# check if pandigital
largest = 0
for i in primes:
    if not primes[i]:
        continue
    else:
        exists = []
        temp = str(i)
        numOfDigits = len(temp)
        for letter in temp:
            num = int(letter)
            if letter in exists or num > numOfDigits or num == 0:
                exists.clear()
                break
            else:
                exists.append(letter)

        if len(exists) != 0 and i > largest:
            largest = i

print(largest)


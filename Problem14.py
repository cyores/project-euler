
def SolveSeq(n):
    chainLength = 0
    startN = n

    while n != 1:
        if n % 2 == 0:
            n /= 2
            chainLength += 1
            if n in seen:
                chainLength += seen[n]
                break
            else:
                continue
        else:
            n = (3 * n) + 1
            chainLength += 1
            if n in seen:
                chainLength += seen[n]
                break
            else:
                continue

    if startN not in seen:
        seen[startN] = chainLength

    return chainLength

n = 1
longestChainNum = 0
longestChain = 0

seen = {1: 1} # dict(n: chainLength) to store the chain length of numbers so we dont have to recalculate them

while n < 1000000: # 1 000 000
    solved = SolveSeq(n)
    if solved > longestChain:
        longestChain = solved
        longestChainNum = n
    n += 1

print('The longest chain belongs to', longestChainNum, 'with a length of', longestChain)

# runs in 59 seconds without the dictionary
# runs in 4.5 with the dictionary


def isSparse(n):
    # Your code here
    conSecOnes = 0
    conSecZeros = 0
    while n > 0:
        rightShift = n >> 1
        if (rightShift & 1) == 1:
            conSecOnes += 1
        if (rightShift ^ 0) == 0:
            conSecZeros += 1
        if conSecOnes > 1 or conSecZeros > 1:
            return 1
        n = n & (n-1)
    return 0


print(isSparse(2))

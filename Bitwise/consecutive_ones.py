def maxConsecutiveOnes(N):
    res = 0
    tempCount = 0
    while(N > 0):
        if (N & 1) == 1:
            tempCount += 1
        else:
            tempCount = 0
        res = max(res, tempCount)
        N = N >> 1
    return res
print(maxConsecutiveOnes(14))
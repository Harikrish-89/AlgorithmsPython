import math

def maxAnd(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            res = max(res, arr[i] & arr[j])
    return res


arr = [4, 8, 12, 16]
print(maxAnd(arr))

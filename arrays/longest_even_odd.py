def longest_even_odd(arr):
    curr_len = 1
    res = 1
    for idx in range(0,len(arr)-1):
        if arr[idx]%2==0 and arr[idx+1]%2 == 0:
            res = max(res, curr_len)
            curr_len = 1
        else:
            curr_len += 1
    return max(res, curr_len)

print(longest_even_odd([5,10,20,6,3,8]))

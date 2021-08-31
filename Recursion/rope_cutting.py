def max_ways(len, a, b, c):
    if len == 0:
        return 0
    if len == -1:
        return -1
    max_cut = max(max_ways(len-a, a, b, c), max_ways(len-b, a, b, c), max_ways(len-c, a, b, c))
    return max_cut if max_cut == -1 else max_cut + 1

print(max_ways(5,2,2,1)) 
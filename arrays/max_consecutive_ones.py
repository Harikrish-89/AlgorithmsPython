def find_max_consecutive_ones(arr):
    max_consec_ones = 0
    current_consec_ones = 0
    for elm in arr:
        if elm  == 1:
            current_consec_ones += 1
        else:
            max_consec_ones = max(max_consec_ones, current_consec_ones)
            current_consec_ones = 0
    return max(max_consec_ones, current_consec_ones)

print(find_max_consecutive_ones([1,1,1,1,1,1,1,1,1,1,1,1,1]))
        

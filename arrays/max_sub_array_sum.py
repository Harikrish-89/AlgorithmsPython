def kadanes_algo(arr):
    max_sum_arr = [0 for x in range(0, len(arr))]
    max_sum_arr[0] = arr[0]
    for elm_index in range(1, len(arr)):
        max_sum_arr[elm_index] = max(arr[elm_index], arr[elm_index]+ max_sum_arr[elm_index-1])
    return max(max_sum_arr)

print(kadanes_algo([-2,1,-3,4,-1,2,1,-5,4]))

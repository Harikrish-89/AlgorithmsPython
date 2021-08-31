def max_circular_sub_array_sum(arr):
    max_normal = kadanes(arr)
    max_circular = sum(arr) + kadanes([-x for x in arr])
    ans = max(max_normal, max_circular)
    print(ans)

def kadanes(arr):
    max_sum_arr = [0 for x in range(0, len(arr))]
    max_sum_arr[0] = arr[0]
    for elm_index in range(1, len(arr)):
        max_sum_arr[elm_index] = max(arr[elm_index], arr[elm_index]+ max_sum_arr[elm_index-1])
    return max(max_sum_arr)

max_circular_sub_array_sum([5,-2,3,4])
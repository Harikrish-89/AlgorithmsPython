def is_array_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


print(is_array_sorted([1,3,2,4,5]))
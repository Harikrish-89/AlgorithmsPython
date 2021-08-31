def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int((low + high)/2)
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary_search_recursive(arr, x, low, high):
    mid = int((high + low)/2)
    if low > high:
        return -1
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        high = mid-1
        return binary_search_recursive(arr, x, low, high)
    else:
        low = mid + 1
        return binary_search_recursive(arr, x, low, high)
    return -1
    
print(binary_search([10,20,30,40,50,70],90))

input_arr = [10,20,30,40,50,70]
print(binary_search_recursive(input_arr,35, 0, len(input_arr)-1))

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    print(arr)

reverse_array([1,2,4,5,6])
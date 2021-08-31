def left_rotate(arr, n):
    temp = arr[0:n]
    res = arr[n:len(arr)]
    res = res + temp 
    print(res)

left_rotate([1,2,3,4,5], 4)
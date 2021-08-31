def move_zeros(arr):
    zp=0
    for index in range(0,len(arr)):
        if arr[index] != 0:
            temp = arr[zp]
            arr[zp] = arr[index]
            arr[index] = temp
            zp +=1
    print(arr)

       
 
move_zeros([1,2,0,0,3,5])
        
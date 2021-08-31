def leaders_in_array(arr):
    res = []
    local_max = -1
    for index in range(len(arr)-1, -1, -1):
        if(arr[index] > local_max):
            res.append(arr[index])
            local_max = arr[index]
    print(res)





leaders_in_array([7,10,4,3,6,5,2])

leaders_in_array([10,20,30])

leaders_in_array([30,20,10])
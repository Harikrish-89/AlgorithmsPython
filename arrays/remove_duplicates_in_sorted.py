def remove_duplicates(arr):
    print(set(arr))

remove_duplicates([1,1,2,2,4,5])

def remove_duplicates_iterative(arr):
    i = 0
    for index in range(1, len(arr)):
        if(arr[index] != arr[i]):
            i+=1
            arr[i] = arr[index]
    print(arr)

remove_duplicates_iterative([1,1,1,2,2,2,3,3,3])
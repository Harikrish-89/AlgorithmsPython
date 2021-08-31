def count_of_subsets(arr, k, index, cur):

    if len(arr) == index:
        return 1 if sum(cur) == 1 else 0
   
    return  count_of_subsets(arr, k, index+1, cur) + count_of_subsets(arr, k, index+1, cur + [arr[index]])

a= []
print(count_of_subsets([1,2], 2, 0, a))
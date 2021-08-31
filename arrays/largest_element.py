def find_largest(arr):
    max=0
    max_index = -1
    for index, elem in enumerate(arr):
        if elem > max:
            max = elem
            max_index = index
    return max_index

print(find_largest([1,4,5,6]))

print(max([1,2,3,4,5]))

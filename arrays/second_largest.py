def second_largest(arr):
    max_index = -1
    max = -1
    second_max = -1
    second_max_index = -1
    for index, elem in enumerate(arr):
        if elem > max and elem > second_max:
            second_max = max
            second_max_index = max_index
            max = elem
            max_index = index
        elif elem > second_max and elem < max:
            second_max = elem
            second_max_index = index
    return second_max_index


print(second_largest([20,40,49,29]))
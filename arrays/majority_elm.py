def majority_elm(arr):
    times = len(arr)/2 + 1
    count_map = {}
    for elm in arr:
        if elm in count_map:
            count_map[elm] += 1
        else:
            count_map[elm] =  1
    print (max(count_map, key=count_map.get))

majority_elm([8,7,6,8,6,6,6,6])

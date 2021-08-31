def trapping_rain_water(height):
    left_max = []
    right_max = []
    left_max_curr = height[0]
    left_max.append(left_max_curr)
    right_max_curr = height[len(height)-1]
    right_max.append(right_max_curr)
    rain_trapped = 0
    for elm in range(1, len(height)):
        left_max_curr = max(height[elm], left_max_curr)
        left_max.append(left_max_curr)
    for elm in range(len(height)-2, -1, -1):
        right_max_curr = max(height[elm], right_max_curr)
        right_max.append(right_max_curr)
    for elm in range(1, len(height)-1):
        rain_trapped += min(left_max[elm], right_max[elm])-height[elm]
    print(left_max,":",right_max)
    return rain_trapped


print(trapping_rain_water([0,2,0]))

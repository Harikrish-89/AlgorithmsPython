from typing import Counter


def is_lucky_number(n):
    series = [i for i in range(1,n+1)]
    counter = 2
    print(series)
    while counter < len(series)+2:
        del series[counter-1::counter]
        print(series)
        counter += 1
    return n in series

    


print(is_lucky_number(73))
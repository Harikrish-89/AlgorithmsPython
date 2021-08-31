import sys
def stock_buy_sell(arr):
    profit = 0
    for index in range(1, len(arr)):
        if arr[index] > arr[index-1]:
            profit +=  arr[index]- arr[index-1]
    print(profit)



stock_buy_sell([1,2,5,3,2,8,12])

stock_buy_sell([30,20,10])

stock_buy_sell([10,20,30])
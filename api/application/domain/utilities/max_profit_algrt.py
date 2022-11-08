def max_profit(prices: list, days: int) -> int:
     
    profit = 0
 
    for i in range(1, days):
 
        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:
 
            # difference added to 'profit'
            profit += prices[i] - prices[i-1]
 
    return profit
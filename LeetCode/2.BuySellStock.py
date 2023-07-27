class Solution (object):    
    
    def max_profit(price_list: list[int]) -> int:

        # Return 0 if the trade day is less than 2 days
        if len(price_list) < 2: return 0

        #Calculate max profit
        max_profit: int = 0            
        for buy_day, buy_price in enumerate(price_list):            
            
            price_list_after_buy_day = price_list[buy_day:]
            sell_price = max(price_list_after_buy_day)
            profit = sell_price - buy_price
            
            if profit>max_profit: max_profit=profit

        
        return max_profit


       

def main() -> None:
    
    prices = [[7,1,5,3,6,4],
              [7,6,4,3,1],
              [2,4,1],
              [0],
              [1,2],
              [3,2,6,5,0,3]]
    profits = [5,0,2,0,1,4]
    
    for index, test in enumerate(prices):
        print (f"\nThe price list is: {prices[index]}")
        print (f"The expected maximum profit is: {profits[index]}")
        print (f"The calculated maximum profit is: {Solution.max_profit (price_list=prices[index])}")
    

if __name__ == "__main__":
    main()
        
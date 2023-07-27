class Solution (object):    
    
    def max_profit(price_list: list[int]) -> int:

        # Return 0 if the trade day is less than 2 days
        if len(price_list) < 2: return 0

        # Calculate max profit
        profit = 0
        buy_price = price_list[0]          
        
        for day in range(len(price_list)):
            buy_price = min(buy_price, price_list[day]) 
            profit = max(profit, price_list[day]-buy_price)
        
        return profit


       

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
        
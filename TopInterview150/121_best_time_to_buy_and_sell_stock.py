class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        T.C -> O(n)
        S>C -> O(1)
        Could not crack it
        This is an easy Dynamic programming solution: In this question the hard part was to understand that we need two things max_value and min_value to calulate highest profit and min_value should always be before max (since you cannot sell a stock before buying) therefore, what we do it sotre the min_value as we go and keep calculating the profit adn we go and we maintain the nim value and max profit as we go. In this case, it will never be possible that we get profit zero as the first step we set he profit as zero by doing prices[i] - min_value e.g = 7 - 7  = 0. Now there might be possiblity that min_value is greater than prices[i] but it will not be replaced at the max_profit.
        """

        profit = 0
        max_profit = 0
        min_value = prices[0]
        for i in range(len(prices)):

            profit = prices[i] - min_value
            min_value = min(min_value, prices[i])
            max_profit = max(profit, max_profit)
        
        return max_profit


            















        
        
#         min_el = prices[0]
#         profit = 0
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < min_el:
#                 min_el = prices[i]
#                 print("min_element", min_el)
#             profits = prices[i] - min_el
#             max_profit = max(profits, max_profit)
#         return max_profit
            
            















        
#         max_profit = 0
#         min_value = prices[0]
#         diff = 0
#         for i in range(len(prices)):
#             diff = prices[i] - min_value
#             if min_value > prices[i]:
#                 min_value = prices[i]
#             if max_profit < diff:
#                 max_profit = diff
#         return max_profit

            

            















#         # min_price = prices[0]
#         # max = 0
#         # diff = 0
#         # for i in range(len(prices)):
#         #     profit = prices[i] - min_price
#         #     if max < profit:
#         #         max = profit
#         #     if min_price > prices[i]:
#         #         min_price = prices[i]
#         # return max
            
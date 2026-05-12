class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        """
        In this question we used dict as an table for optimization the dfs solution to memoization solution. We explore all path hold and buy or sell. The part I got stuck was basically how to reduce the 3 parameters to two. Basically profit parameter we do not need actually as it can be calculated as we call the function. THink aobut this agaon as you ahve been stuck with this before as well.
        T.C -> O(2n)
        S.C -> O(2n)
        Top down approch ofr dp done, next time do the bottom up approch real dp.

        """
        dp = {}
        def dfs(i, buy):
            if i > len(prices) - 1:
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            profit1 = dfs(i + 1, buy)
            if buy:
                profit2 = dfs(i + 1, not buy) - prices[i]
                dp[(i, buy)] =  max(profit1, profit2)
            else:
                profit3 = dfs(i + 1, not buy) + prices[i]
                dp[(i, buy)] = max(profit1, profit3)
            return dp[(i, buy)]
            
            
        return dfs(0, True)


    #     dp = {}


    #     def dfs(i, buy):
    #         if len(prices) == i:
    #             return 0
            
    #         if (i, buy) in dp:
    #             return dp[(i, buy)]

    #         if buy:
    #             max_profit = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
    #         else:
    #             max_profit = max(dfs(i + 1, True) + prices[i], dfs(i + 1, False))
            
    #         dp[(i, buy)] = max_profit
    #         return max_profit

    #     return dfs(0, True)




    # dp = [[0, 0] for _ in range(n + 1)]
        
    #     # Base case: dp[n][0] = dp[n][1] = 0 (no days left, no profit)
    #     # Already initialized to 0
        
    #     # Fill from day n-1 back to day 0
    #     for i in range(n - 1, -1, -1):
    #         # If we can buy: either skip or buy today
    #         dp[i][1] = max(dp[i + 1][1], dp[i + 1][0] - prices[i])
            
    #         # If we can sell: either skip or sell today
    #         dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] + prices[i])
        
    #     return dp[0][1]  # Start at day 0, allowed to buy
        
        
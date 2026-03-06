
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        dp[0][0] = 0

        for i in range(len(coins)):
            dp[i][0] = 1
        
        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0

        for i in range(1, len(coins)):

            for j in range(1, amount + 1):

                skip = dp[i - 1][j]
                include = 0
                if j - coins[i] >= 0:
                    include = dp[i][j - coins[i]]  # not + 1 because we ahve to addd skip and include if we include that means that for this new target if I inlcude this, I can acheive this by this many ways which dp[i][j - coins[i]], so you dont ahve to do + 1, instead you jsut add skip at the end
                
                dp[i][j] = skip + include
            
        return dp[len(coins) - 1][amount] if dp[len(coins) - 1][amount] != -1 else 0


        """
        Unbounded Knapsack simple problem we use memoization we just ahve to count the ways of getting to targett so we did not use max or min. Simply just add
        """


        # dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        # def dfs(i, curr_amt):

        #     if curr_amt == amount:
        #         return 1
        #     if i >= len(coins) or curr_amt > amount:
        #         return 0
            
        #     if dp[i][curr_amt] != -1:
        #         return dp[i][curr_amt]
 
        #     dp[i][curr_amt] = dfs(i + 1, curr_amt)

        #     if amount - curr_amt + coins[i] >= 0:
        #         dp[i][curr_amt] += dfs(i, curr_amt + coins[i])
        #     # print(i, curr_amt)
        #     return dp[i][curr_amt] 
        
        # return dfs(0, 0)

            













        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for i in range(len(coins)):
        #     nextdp = [0] * (amount + 1)
        #     nextdp[0] = 1

        #     for j in range(1, amount + 1):
        #         nextdp[j] = dp[j]
        #         if j - coins[i] >= 0:
        #             nextdp[j] += nextdp[j - coins[i]]
        #     dp = nextdp
        
        # return dp[amount]












        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for i in range(len(coins) -1, -1, -1):
        #     nextdp = [0] * (amount + 1)
        #     nextdp[0] = 1
        #     for j in range(1, amount + 1):

        #         nextdp[j] = dp[j]
        #         if j - coins[i] >= 0:
        #             nextdp[j] += nextdp[j - coins[i]]
        #     dp = nextdp
        # return dp[amount]
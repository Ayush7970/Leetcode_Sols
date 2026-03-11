from typing import List
class Solution:


    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        """
        Tabular approach of Unbounded knapsack problem. In this problem we can include the same item multiple times. So in the dp table when we include the item we do not move to next index rather we stay on the same index i to include it again.
        """
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]
        
        for i in range(capacity + 1):
            if i >= weight[0]:
                dp[0][i] = profit[0]

        for i in range(len(profit)):
            for c in range(capacity + 1):
                skip = dp[i - 1][c]
                include = 0
                if c - weight[i] >= 0 :
                    include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(skip, include)
                

        print(dp)
        return dp[len(profit) - 1][capacity]


    """
    Memoized approach of Unbounded knapsack problem. In this problem we can include the same item multiple times. So in the recursive call when we include the item we do not move to next index rather we stay on the same index i to include it again.
    T.C -> O(n * capacity)
    S.C -> O(n * capacity) + O(n) for recursion stack
    """
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        
        dp = [[-1] * (capacity + 1) for _ in range(len(profit))]
        def dfs(i, curr_capacity):

            if i == len(profit) or curr_capacity == 0:
                return 0
            
            if dp[i][curr_capacity] != -1:
                return dp[i][curr_capacity]

            dp[i][curr_capacity] = dfs(i + 1, curr_capacity)

            if curr_capacity - weight[i] >= 0:

                dp[i][curr_capacity] = max(dp[i][curr_capacity], profit[i] + dfs(i, curr_capacity - weight[i]))
            
            return dp[i][curr_capacity]
        
        return dfs(0, capacity)
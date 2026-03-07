from collections import defaultdict
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Bottom up approach for unbounded knapsack. You have to have dp[0] = 0 for base case. Espicially for dp[j] not for dp[new_j]
        """

        arr = [1, 7, 30]
        INF = 10**15
        dp = [INF] * (len(days) + 1)
        dp[0] = 0

        def next_day_func(i, till_day):
            curr = days[i] + till_day - 1
            while i < len(days) and curr >= days[i]:
                i += 1
            return i

        j = 0

        for j in range(len(days)):
            for i in range(len(costs)):
                new_j = next_day_func(j, arr[i])
                dp[new_j] = min(dp[new_j], dp[j] + costs[i])

        return dp[len(days)]



        """
        This is not proper unbounded knapsack problem but we tried to solve it that way but then we olve it the different way in dp. Since we did not need the i for the cost the table we will form will be 1D and so we cna simply create a dictionary for memoization.
        """
        # dp = {}
        # def next_day_func(i, till_day):

        #     curr = days[i] + till_day - 1

        #     while i < len(days) and curr >= days[i]:

        #         i += 1

        #     return i

        # def dfs(i):

        #     if i == len(days):
        #         return 0
            
        #     if i in dp:
        #         return dp[i]

        #     result1 = costs[0] + dfs(next_day_func(i, 1))
        #     result2 = costs[1] + dfs(next_day_func(i, 7))
        #     result3 = costs[2] + dfs(next_day_func(i, 30))

        #     dp[i] =  min(result1, result2, result3)
        #     return dp[i]

        # return dfs(0)



        
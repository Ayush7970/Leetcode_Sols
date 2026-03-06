from typing import List
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) +1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total - nums[i]] += count
                dp[i + 1][total + nums[i]] += count
        
        return dp[len(nums)][target]

        # """
        # Time Complexity -> O(n * m)
        # Space Complexity -> O(n * m)
        # This is dp: knapsack algorithm. In this question I have taken the approach of top down memoization approach. In this question I simply applied the dfs approach and then added the cached the meoiation dictioanry. We added the dictioanry as the target is not bounded adn there are negative values in this array.
        # """
        # # n = len(nums)
        # # result = 0
        # # memo = {}  # dictioanry is good when you have negatives and not bounded target, like in this case (i, val)
        # # def dfs(i, val_sum):
        # #     if val_sum == target and i == n:
        # #         return 1
        # #     if i >= n:
        # #         return 0
        # #     if (i, val_sum) in memo:
        # #         return memo[(i, val_sum)]

        # #     memo[(i, val_sum)] = (dfs(i + 1, (-1 * nums[i]) + val_sum) + dfs(i + 1, nums[i] + val_sum))
        # #     return memo[(i, val_sum)]
        # # return dfs(0, 0)

        # """
        # Now trying dp : knapSack Bottom up approach. In this problem we create a dictionaries in side the list. That is a 2d table. What we do is basically we store 1 at dp[0][0] and then we loop throgh that dictonary and start storing all the sum as keys and count as values, as we move forward we keep on shifting the defaultdict to next dicts by writing dp[i + 1] and then at the end we will have all our values acumulated. That's why we return dp[n][target]
        # """

        # n = len(nums)
        # dp = [defaultdict(int) for i in range(n + 1)]
        # dp[0][0] = 1

        # for i in range(n):

        #     for total, count in dp[i].items():
        #         dp[i + 1][total - nums[i]] += count
        #         dp[i + 1][total + nums[i]] += count

        # return dp[n][target]




        

        
 

















        # # dp = defaultdict(int)

        # # dp[0] = 1
        # # for i in range(len(nums)):

        # #     nextdp = defaultdict(int)

        # #     for curr_sum, count in dp.items():
        # #         nextdp[curr_sum + nums[i]] += count
        # #         nextdp[curr_sum - nums[i]] += count
        # #     dp = nextdp 
        
        # # return dp[target]
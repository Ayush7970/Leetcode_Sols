from collections import defaultdict
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Practiced again created both solution on my own, oen with memoization and one with pure dp
        T.C -> O(n^2)
        S.C -> O(n)
        But there is a better solution which solves oin T.C O(n) and S.C O(1). the intuition is build on BFS and exploring the farthest point adn increasing the count when the limit is exhauasted. Solution is just below 
        
        """ 
        # best solution for this problem 
        current_end, farthest, jump = 0, 0, 0

        for i in range(len(nums) - 1): # you need to go one less
            farthest = max(nums[i] + i, farthest)
            if i == current_end:
                jump += 1
                current_end = farthest
        return jump


        # dp = [float("inf")] * len(nums)
        # dp[len(nums) - 1] = 0
        # game = len(nums) - 1

        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] + i >= game:
        #         game = i
        #         for k in range(i, nums[i] + i + 1):
        #             dp[i] = min(dp[i], 1 + dp[min(len(nums) - 1, k)])
        #     # print(dp, i)

        # return dp[0]



        # dp = {}

        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return 0 
        #     if i in dp:
        #         return dp[i]
        #     ans = len(nums)
        #     for j in range(1, nums[i] + 1):
        #         ans = min(ans, 1 + dfs(i + j))
        #     dp[i] = ans
        #     return dp[i] 
        
        # return dfs(0)







#         """
#         Practice 1, created this olsutio form the back on my own. Correct solution and this is greedy approach
#         """

#         dp = [float("inf")] * len(nums)
#         dp[len(nums) - 1] = 0
#         i = len(nums) - 2

#         while i >= 0:
            
#             for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
#                 dp[i] = min(dp[i], 1 + dp[j])

#             i -= 1
#         return dp[0]


# # class Solution:
# #     def jump(self, nums: List[int]) -> int:
# #         count = 0
# #         left = right = 0
# #         while right < len(nums) - 1:
# #             farthest = 0
# #             for i in range(left, right + 1):
# #                 farthest = max(nums[i] + i, farthest)
# #             left = right + 1
# #             right = farthest
# #             count += 1
# #         return count

        
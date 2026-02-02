class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # practice 1
        target = sum(nums)
        if target % 2 != 0:
            return False
        
        target = target // 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]

        for i in range(target + 1):
            dp[0][i] = True if (i == nums[0]) else False 
            
        for i in range(len(nums)): dp[i][0] = True
        
        for i in range(1, len(nums)):
            for t in range(1, target + 1):

                dp[i][t] = True if dp[i - 1][t] or (t - nums[i] >= 0 and dp[i - 1][t - nums[i]]) else False

        # print(dp)
        return dp[len(nums) - 1][target]


        # """
        # this solution is DP: pure top Down approach (memoization) (Knapsack). In thisw appraoch First we ahve to decide the decision tree. This is a Knapsack(0/1) Algorithm problem in which you pick or you use skip. So you create a two choice decision tree in this. Then  second we have to decide what are the moving variable in the recursion taht are i and current_sum, so thats how I know that we need to 2D table as well for memoization. 
        # """
        # # n = len(nums)
        # # total = sum(nums)
        # # target = total // 2

        # # if total % 2 != 0:
        # #     return False

        # # memo = [([-1] * (target + 1)) for i in range(n + 1)]

        # # def dfs(i, target):
        # #     if target == 0:
        # #         return True
            
        # #     if  target < 0 or i >= n:
        # #         return False
            
        # #     if memo[i][target] != -1:
        # #         return memo[i][target]
            
        # #     memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))

        # #     return memo[i][target]
    
        # # output = dfs(0, target)
        # # return output 


        # """
        # This is another solution of The Dp: knapSack problem in bottom up approach (tabulation solution). In this problem we have our base case as nums[0] and nums[i][0] the first row will be False as target cannot be achieved with value 0 and first column will be True as 0 can be achevied at any point by not including any element. Then we loop from beginning to the end from 1,1 to end and the end value will have our result.
        # """

        # total = sum(nums)
        # target = total // 2
        # n = len(nums)
        # if total % 2 != 0:
        #     return False
        
        # dp  = [([False] * (target + 1)) for i in range(n + 1)]

        # for i in range(n + 1):    # for 0 target all we be True from the base case
        #     dp[i][0] = True

        # for i in range(1, n + 1):   # we start from 1 because all the dp[0] will be False as 0      
        #     for t in range(1, target + 1):
        #         if nums[i - 1] <= t:
        #             dp[i][t] = (dp[i - 1][t] or dp[i - 1][t - nums[i - 1]])
        #         else:
        #             dp[i][t] = dp[i - 1][t]
        # return dp[n][target]



        # # target = sum(nums) // 2
        # # if sum(nums) % 2 != 0:
        # #     return False
            
        # # dpset = set()
        # # dpset.add(0)
        # # for i in range(len(nums) - 1, -1, -1):

        # #     nextdp = set()
        # #     for d in dpset:
        # #         nextdp.add(d + nums[i])
        # #         nextdp.add(d)
        # #     dpset = nextdp

        # # return True if target in dpset else False






















        # # if sum(nums) % 2 != 0:
        # #     return False
        
        # # dp = set()
        # # dp.add(0)
        # # for i in range(len(nums)-1, -1, -1):
        # #     nextdp = set()
        # #     for num in dp:
        # #         nextdp.add(num +nums[i])
        # #         nextdp.add(num)
        # #     dp = nextdp 
        # # return True if (sum(nums) // 2) in dp else False

        
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        Try Again
        Greedy Problem: I tried with dfs and memoized dfs both of them did not passed for time complexity. The trick was greedy. You simply ahve to loop form the back and check if the i + nums[i] is reachable to the goal then i is the new goal. Simple greedy, breaking down the problem from the back. LEARN THIS TECHNIQUE.
        """

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False



    #     goal = len(nums) - 1

    #     for i in range(len(nums)- 1, -1, -1):
    #         if nums[i] + i >= goal:
    #             goal = i
    #     return True if goal == 0 else False

        
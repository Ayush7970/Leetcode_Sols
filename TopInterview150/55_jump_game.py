class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        I cracked it this time. This was a greedy questions and I used the approach of traversing from the back. 
        T.C -> O(n)
        S.C -> O(1)
        """

        location = len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i + 1 + nums[i] >= location:
                location = i + 1
            
        return True if location == 1 else False

        # practice 1 Greedy, identfied start from back
        # goal = len(nums) - 1

        # for i in range(len(nums) - 1, -1, -1):

        #     if i + nums[i] >= goal:
        #         goal = i
        
        # return True if not goal else False







    #     """
    #     Try Again
    #     Greedy Problem: I tried with dfs and memoized dfs both of them did not passed for time complexity. The trick was greedy. You simply ahve to loop form the back and check if the i + nums[i] is reachable to the goal then i is the new goal. Simple greedy, breaking down the problem from the back. LEARN THIS TECHNIQUE.
    #     """

    #     goal = len(nums) - 1

    #     for i in range(len(nums) - 1, -1, -1):
    #         if i + nums[i] >= goal:
    #             goal = i
        
    #     return True if goal == 0 else False



    # #     goal = len(nums) - 1

    # #     for i in range(len(nums)- 1, -1, -1):
    # #         if nums[i] + i >= goal:
    # #             goal = i
    # #     return True if goal == 0 else False

        
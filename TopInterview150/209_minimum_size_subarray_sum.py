class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """
        Practice 1, solution below
        """

        i, j = 0, 0
        sum1 = nums[0]
        min_count = float("inf")
    
        while j < len(nums) and i <= len(nums):
                
            if sum1 < target and j != len(nums) -1:
                j += 1
                sum1 += nums[j]

            elif sum1 >= target:
                min_count = min(min_count, j - i + 1)
                sum1 -= nums[i]
                i += 1
            else:
                break
        
        return min_count if min_count != float("inf") else 0
            


                

            














    #     """
    #     This is a simple variable sliding window problem in which we have to move the two move the left pointer only when we exceed the sum so that we can get minimum length everytime. when we move the left poitner we also ahve the reduce the sum as we ahve to maintian the current sum of the window between both the pointers.
    #     """

    #     min_length = float('inf')
    #     left = 0 
    #     current_sum = 0
    #     for right in range(len(nums)):

    #         current_sum += nums[right]
    #         while current_sum >= target:                    # moving the left pointer if the sum in les than the target
    #             min_length = min(min_length, right - left + 1)
    #             current_sum -= nums[left]
    #             left += 1

    #     return min_length if min_length != float('inf') else 0
            
                


            


        
        
from collections import defaultdict
from ast import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        Another great question, in which I failed. I kind of got the correct idea of going first with a for loop and count the duplicates with a while loop within. But I did not thought that I still need a for loop to replace the value.

        Solution : Simply loop through the array and then in the while loop count the duplicates and then replace the minnimum 2 or 
        T.C -> O(2n)
        S.C -> O(1)
        """

        count = 0 
        l = 0
        r = 0
        while r < len(nums):
    
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l

        # for i in range(1, len(nums)):
        #     num = nums[i]


        #     if nums[i - 1] == nums[i]:
        #         print("check", nums[i], i)

        #         j = i + 1
        #         while j < len(nums) and nums[j] == nums[i]:
        #             j += 1
                
        #         temp = nums[j]
        #         nums[j] = nums[i + 1]
        #         nums[i + 1] temp

        #         i += 1
            
        # return 1





        

















        
        """
        This is a really good question of two pointer approach, in this question I am basically using a dictionary to maintain the count of the numbers, if it greater than than i only move the right pointer and left pointer stays where it needs to switch the place with and when we find a elements who count is less than two then we repalce it wit hthe left pointer and increase the count
        """

        # left, right = 0, 0
        # count = {}
        # while right < len(nums):
        #     if nums[right] not in count or count[nums[right]] < 2:
        #         if nums[right] not in count:
        #             count[nums[right]] = 1
        #         else:
        #             count[nums[right]] += 1
        #         nums[left] = nums[right]
        #         left += 1
        #     right += 1
            
        # return left
        
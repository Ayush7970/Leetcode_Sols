
from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        """
        two apporaches same time and space complexity

        1. In this approach even the time complexity and the space complexity is same the issue is that it moves all the correct elements unnecessarly for example 41235 and val = 4
        """
    
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        return j

        """
        2. This is the second approach in which if we found the element at i we replace it with the last element and worst case if the last element was itself the element then it is fine since we update n after that and not i so it will be update in the next iteration.
        """


        n = len(nums) - 1
        i = 0
        while i <= n:

            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1
        
        return n + 1


        

        
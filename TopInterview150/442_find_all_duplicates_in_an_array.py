
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        """
        Beautiful Question! This is called IQ
        Very good question: Definately try again
        All about Array. In the question you know all the elements are with the range till n. So you can use the array's indexing itself as an dictionary for marking.
        """

        res = []
        for num in nums:

            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        
        return res

        
        

        

from ast import List



class Solution:
    def maxArea(self, height: List[int]) -> int:

 

        """
        This is also a good two pointer approach, In this bascially we are having two pointer from left and right where you move the the one which is low so that we always get the max size. Moreover, We calculate the area by mulitply the breath with the minimun height.
        """
        
        left, right = 0, len(height) - 1
        max_size = 0
        max_size = max(max_size, (right - left) * min(height[left], height[right]))
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left  += 1
            max_size = max(max_size, (right - left) * min(height[left], height[right]))
        return max_size



















        # i = 0
        # j = len(height) - 1
        # maxarea = 0
        # max_index = 0
        # while i < j:

        #     area = min(height[i], height[j]) * (j - i)
        #     if maxarea < area:
        #         maxarea = area
            
        #     if height[j] >= height[i]:
        #         i += 1
        #     else:
        #         j -= 1
        
        # return maxarea
            











        # # i = 0
        # # j = len(height) - 1
        # # maxarea = 0
        # # while i < j:
        # #     area = min(height[i], height[j]) * (j - i)
        # #     maxarea = max(maxarea, area)
        # #     if height[i] >= height[j]:
        # #         j -= 1
        # #     else:
        # #         i += 1

        # # return maxarea
        
        

from ast import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        """
        Pretty good question: MAth Geometry type. The important part of the question was the slope. I got confused by adding and subtracting the which basically works in table. I got a bit confused in it. The slope can be in angle not jst 45, 90, 180, 0. Therefore, we use the equation formula of slope.
        Morever, one of the important part was also the fact that two different line one above each other can still have the same slope. This problem is overc omed easly in neetcode solution. Since he calculate slope for one point for all other points and then he store the result to max simontaneously and reset the dictionary wheere slope were stored. Therefore, there was no porblem with 2 lines on different height or breath still having same slope. 
        """

        res = 1
        for i in range(len(points)):
            count = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 - x2 == 0:      # dealing with if the slope is of a vertical line which is undefined
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res



        
         


        
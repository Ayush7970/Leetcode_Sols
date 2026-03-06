from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        """
        One of the top 150 interview questions, belongs to the category of Intervals.
        """

        points.sort(key=lambda x: x[1]) # sorting by end key

        count = 0
        x1, x2 = points[0]
        range1 = x2
        i = 1
        count = 1
        while i < len(points):
            
            y1, y2 = points[i]

            if y1 > range1:
                count +=1
                range1 = y2
            else:
                range1 = min(range1, y2)
            i += 1

        return count
        
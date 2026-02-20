class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        """
        This is practice solution. Perfect solution is below this. These clearly explains which level you think and neetcode thinks. In the perfect solution, the main important adn the tricky aprt they did was they updated the newInterval everytime it clashed with a interval and they updated the new outer bounds in the newInterval. This way there was no problem of adding the rest over intervals or issue of duplicate intervals. Great solution. I did it by trial and error with test cases.
        """
        # if not intervals:
        #     return [newInterval]
        # res = []

        # new_start, new_end = newInterval
        # i = 0
        # while i < len(intervals):

        #     start, end = intervals[i]            

        #     if new_end < start:
        #         res.append([new_start, new_end])
        #         res.extend(intervals[i:])
        #         break
        #     elif new_start > end:
        #         res.append([start, end])
        #         if i == len(intervals) - 1:
        #             res.append([new_start, new_end])
        #             break
        #     else:
        #         pos1 = min(new_start, start)

        #         j = i
        #         while j < len(intervals) and new_end >= intervals[j][0]:
        #             j += 1

        #         j -= 1
        #         pos2 = max(new_end, intervals[j][1])

        #         res.append([pos1, pos2])
        #         res.extend(intervals[j + 1:])
        #         break
        #         i = j
        #     i += 1
            
        
        # return res














        # res = []

        # for i in range(len(intervals)):

        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        # res.append(newInterval)
        # return res 

                  

        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        Array: Interval question. In this question you have to remember that multiple intervals can be converted into one. So the best thing is to create a interval and keep upgrading it with all the intervals that clashes and when does not clash you add it to the array. This is a common apporach when you deal with intervals. 
        T.C -> O(n)
        S.C -> O(1)
        """


        intervals.sort(key=lambda x: x[0]) # by default it does the first value, I just worte for practice
        start, end = intervals[0]
        res = []
        for i in range(len(intervals)):
            curr_s, curr_e = intervals[i]
            if end >= curr_s:
                end = max(end, curr_e)
                start = min(start, curr_s)
            else:
                res.append([start, end])
                start, end = intervals[i]

        res.append([start, end])
        return res

        # intervals.sort(key = lambda i : i[0])
        # output = [intervals[0]]
        # for start, end in intervals[1:]:
        #     if output[-1][1] >= start:
        #         output[-1][1] = max(output[-1][1], end)
        #     else:
        #         output.append([start, end])
        # return output

        # # intervals.sort()
        # # ans = []
        # # for i in range(len(intervals)):
        # #     start = intervals[i][0]
        # #     end = intervals[i][1]
        # #     if len(ans) == 0 or start > ans[len(ans)- 1][1]:
        # #         ans.append([start, end])
        # #     else:
        # #         ans[len(ans)- 1][1] = max(end, ans[len(ans)- 1][1])
        # # return ans















        # # n = len(intervals)
        # # ans = []
        # # intervals.sort()
        # # for i in range(n):
        # #     start = intervals[i][0]
        # #     end = intervals[i][1]
        # #     if ans == [] or start > ans[len(ans)-1][1]:
        # #         ans.append(intervals[i])
        # #     else:
        # #         ans[len(ans)-1][1] = max(end, ans[len(ans)-1][1])  
        # # return ans


             
            
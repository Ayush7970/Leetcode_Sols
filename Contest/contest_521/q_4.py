class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:

        """
        this iquestion was really hard, how we solved this question is we calculated the current meeting revenue and then we just choosed the best revenue from the previous meetings result. So we picked from heap the minimum end time we get obviously lower than the current meeting time. then we keep on getting the max out of it. Then we calculate if current revenue is big or revenue + start + best. best = (previous result - end)

        the statement is result = dp[i] + revenue[j] + (start[j] - end[i])
        so result = revenue[j] + start[j] + (dp[i] - end[i])
        
        """

        meetings.sort()
        ended = []
        ans = 0
        best = float("-inf")
        
        for start, end, revenue in meetings:

            while ended and ended[0][0] <= start:
                e, value = heapq.heappop(ended)
                best = max(value, best)

            dp = revenue

            if best != float("-inf"):
                dp = max(dp, revenue + start + best)

            ans = max(ans, dp)

            heapq.heappush(ended,(end, dp - end))

        return ans
                
                

            
        
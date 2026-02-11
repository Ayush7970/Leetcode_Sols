
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        """
        More better approach, I first sort in reverse = True and then simply check whenever the max_threshold is greater than the count I store the answer otherwise not. 
        T.C -> O(nlogn + n)
        S.C -> O(1)
        """
        citations.sort(reverse=True)
        print(citations)

        max_threshold = 0
        count = 0
        ans = 0
        for i in range(len(citations)):
            count += 1
            max_threshold = citations[i]
            if max_threshold >= count:
                ans = min(max_threshold, count)
        return ans


        """
        Brute force 
        T.C -> O(n^2)
        S.C -> O(1)
        """

        # len_c = len(citations)
        # while len_c > 0:

        #     count = 0
        #     for i in range(len(citations)):
        #         if citations[i] >= len_c:
        #             count += 1
            
        #     if count >= len_c:
        #         return len_c
        #     len_c -= 1
        
        # return 0

        
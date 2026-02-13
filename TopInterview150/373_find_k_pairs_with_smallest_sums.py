from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        """
        Pretty good question. You ahve to identify the topic first which was priority Queue and the tough part was that you have to create the implementation in which you choose either the one left over element or two new element. That is the place where we used the min_heap which basically decides the minimum out of all three of them. 
        """


        min_heap = []
        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        len1 = len(nums1)
        len2 = len(nums2)
        visit = set([0, 0])
        ans = []

        while k > 0 and min_heap:

            sum1, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < len1 and (i + 1, j) not in visit:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visit.add((i + 1, j))

            if j + 1 < len2 and (i, j + 1) not in visit:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visit.add((i, j + 1))
            k -= 1
            
        return ans
        
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        Leetcode's Interview Tip: Whenever you're trying to solve an array problem in place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.
        """
        if m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        

        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            
            if j < 0: # basically if j ends first then you simply end the array2 since array     is correct now i elements should be correctly in place
                break
            if i >= 0 and nums1[i] > nums2[j]:      # this condition should only move forward if i is >= 0 because if not then we know i is finished we can just copy paste array2
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        

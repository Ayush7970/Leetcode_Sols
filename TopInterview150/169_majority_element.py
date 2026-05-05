class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        Welcome to Boter-Moore Voting Algorithm
        T.C -> O(n)
        S.C -> O(1)
        In thhis algorithm we +1 if the element is our candidate and do -1 if not equals to our candidate, we choose candidates as the first element when our count is 0.
        So we start with count 0 and our first element as candidate if the count gets to zero at some point then the next element becomes candidate.
        """

        count = 0
        candidate = None

        for i in range(len(nums)):

            if count == 0:
                candidate = nums[i]
            
            count += 1 if nums[i] == candidate else -1
        
        return candidate

        
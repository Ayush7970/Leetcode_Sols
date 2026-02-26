class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        This is a O(n) space complexity, since python l: and + creates a new list everytime they are used. Check the true O(1) space complexity solution.
        """
        # l = len(nums) - (k % len(nums))
        # nums[:] = nums[l:] + nums[: l]

        """
        O(n) time complexity
        O(1) space complexity
        """
        k %= len(nums)
        def rev(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) - 1)




        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        could not crack it 
        **this belongs to "fast scans, slow writes
        """

        unique_index, replace_index = 1, 1

        while unique_index < len(nums):

            if nums[unique_index] != nums[unique_index - 1]:
                nums[replace_index] = nums[unique_index]
                replace_index += 1
            
            unique_index += 1
        
        return replace_index


        









    #     """
    #     So this is a good two pointer approach. For inplace replace, you use two pointers such that one of them finds the unique element nums[i] != nums[i - 1] and the other keeps track of where that unique element needs to be placed, so the repalce_index only move when we put a unique value in it. 
    #     """

    #     unique_index, replace_index = 1, 1
    #     while unique_index < len(nums):

    #         if nums[unique_index] != nums[unique_index - 1]:
    #             nums[replace_index] = nums[unique_index]
    #             replace_index += 1
            
    #         unique_index += 1
        
    #     return replace_index 

        
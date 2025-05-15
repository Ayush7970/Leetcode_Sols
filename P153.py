class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums) - 1
        low = 0 
        high = n
        min1 = float('inf')
        while low <= high:
            
            if nums[low] < nums[high]:          # if already sorted 
                min1 = min(min1, nums[low])
                break
            
            mid = (low + high) // 2
            min1= min(min1, nums[mid])

            if nums[mid] < nums[low]:   # if it is in left sorted then send to right sorted, vice versa 
                high = mid - 1
            else:
                low = mid + 1
        return min1














        # n = len(nums) - 1
        # low = 0
        # high = n
        # min1 = float('inf')
        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[high] >= nums[low]:
        #         if min1 > nums[low]:
        #             min1 = nums[low]
        #             break
        #     if nums[mid] >= nums[low]:
        #         if min1 > nums[low]:
        #             min1 = nums[low]
        #         low = mid + 1
        #     else:
        #         if min1 > nums[mid]:
        #             min1 = nums[mid]
        #         high = mid - 1 
        # return min1

            

        
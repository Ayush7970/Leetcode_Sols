class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        low = 0 
        high = n 
        while low <= high:
            mid = (low + high) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if target >= nums[low] and nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= nums[mid] and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
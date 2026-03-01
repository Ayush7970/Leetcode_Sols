class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        this is build on the idea of 2 sum Obiviously. The trick is to froze one number. So we can loop through the other two in two sum. So we loop through the k which start fro mfirst and then we preform two sum from 2 to end and then 3 to end. Remember, you cant so the k loop in between of the 2 sum, since then there will be repitation. Moreover, for repitation if k == k - 1 we continue and same for i
        """

        nums.sort()
        ans = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k + 1
            j = len(nums) - 1

            while i < j:

                sum1 = nums[i] + nums[j] + nums[k]

                if sum1 > 0:
                    j -= 1
                elif sum1 < 0:
                    i += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1

                    # practically you only need only one of the loops, since if you find 0 at that value you never gonna fina zero just by moving one element to a new value
                    while j + 1 > 0 and nums[j] == nums[j + 1]:   # you could have doen it for you could have done it for j, its same
                        j -= 1
                    while i - 1 < len(nums) - 1 and nums[i] == nums[i - 1]:   # you could have doen it for you could have done it for j, its same
                        i += 1
                    
        return ans


            
                

        # # nums.sort()
        # # arr = []
        # # for i in range(len(nums)):
        # #     if i > 0 and nums[i] == nums[i - 1]:
        # #         continue
        # #     j = i + 1
        # #     k = len(nums) - 1
        # #     while j < k:
        # #         sum1 = nums[i] + nums[j] + nums[k]
        # #         if sum1 < 0:
        # #             j = j + 1
        # #         elif sum1 > 0:
        # #             k = k - 1
        # #         else:
        # #             list1 = [nums[i], nums[j], nums[k]]
        # #             arr.append(list1)
        # #             j = j + 1
        # #             k = k - 1
        # #             while j < k and nums[j] == nums[j-1]:
        # #                 j = j + 1
        # #             while j < k and nums[k] == nums[k+1]:
        # #                 k = k - 1 

        # # return arr

                    
        
class Solution:
    def candy(self, nums: List[int]) -> int:

        """
        T.C -> O(3n)
        S.C -> O(n)
        This is a greedy Type of Question. The pattern of this question was also Front loop on pass 1 and loop from back on pass 2, like prefix postfix. In this question, we first loop from front and keep increasing the value of each student by prev student + 1 if thier rating is more than prev student, and we do exactly the same for while looping backwards + we also check if the while looping back if the candies distruted are already more more higher rating then we dont increase the value -> ans[i] <= ans[i + 1]
        """

        ans = [1] * len(nums)
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                ans[i] = ans[i - 1] + 1
        

        for i in range(len(nums) - 2, -1, -1):

            if nums[i] > nums[i + 1] and ans[i] <= ans[i + 1]:
                ans[i] = ans[i + 1] + 1
            
        return sum(ans)
            





        #     if ratings[i] < ratings[i+1] and i != len(ratings) - 1:
        #         max_arr.append(1)
        #     else:
        #         max_arr.append(2)
        #         j = len(max_arr) - 1
        #         if len(max_arr) == 1:
        #             continue
        #             # max_arr.append
        #         while j >= 1:
                    
        #             max_arr[j] += 1
        #             if ratings[j] > ratings[j - 1]:
        #                 if max_arr[j] > max_arr[j - 1]:
        #                     continue
        #                 else:
        #                     max_arr[j- 1] += 1
        #             j = j - 1
        # return max_arr
                







        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        Practice 1, solved on my ownm simple prefix and postfix question
        """

        ans = [1] * len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
        
        
        for i in range(len(nums) - 1, - 1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
        


        """
        This is the simple prefix algorithm question in this you simle first ahve to calculate the prefix pro and postfix pro and multiple them. The optimization for this problem is to use only one array instead of different prefix and postfix array.
        """

        n = len(nums)
        result_pro = [1] * n
        product = 1
    
        for i in range(n):
            result_pro[i] *= product
            product *= nums[i]
        
        product = 1
        for i in range(n - 1, -1, -1):
            result_pro[i] *= product
            product *= nums[i]

        return result_pro









        # result = [1] * len(nums)
        # prefix1 = 1
        # suffix1 = 1
        # for i in range(len(nums)):
        #     result[i] *=  prefix1
        #     prefix1 *= nums[i]

        # for i in range(len(nums) - 1, -1, -1):
        #     result[i] *= suffix1

        #     suffix1 *= nums[i]

        # return result

        # # res = [1] * len(nums)
        # # prefix = 1
        # # postfix = 1
        # # for i in range(len(nums)):
        # #     res[i] = prefix
        # #     prefix *= nums[i] 

        # # for i in range(len(nums) -1, -1, -1):
        # #     res[i] *= postfix  
        # #     postfix *= nums[i]
        # # print(postfix) 

        # return res















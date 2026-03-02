class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        """
        Practice 1 with Adbul bari, mathematical concepts. Solved it one ago. Perfectly understnad the question draw the tree and always follow Abdul bari format.
        """
        curr_arr = []
        result = []
        curr_sum = 0
        def dfs(i, curr_sum):

            if curr_sum > target or i >= len(candidates):
                return 
            
            if curr_sum == target:
                new_arr = curr_arr.copy()
                result.append(new_arr)
                return

            # print(i, curr_arr)
            curr_arr.append(candidates[i])
            dfs(i, curr_sum + candidates[i])
            # print(i, curr_arr, "backtracking")
            curr_arr.pop()
            dfs(i + 1, curr_sum)

        
        dfs(0, 0)
        return result


    #     """
    #     This is the backtracking question of type combination. In this question  as always you have to first decide the most optimized tree. The most optimize tree is to take two options whether to add the number or not. This prevents duplicates. You can choose a nubmer multiple times but order is differnet and frequency is same then it is a duplicate Understnad the decision tree properly. If you cant. Then it is just base cases and condition.
    #     """

    #     result = []
    #     combinations = []

    #     def recursive_func(index, total_sum):

    #         if total_sum == target:
    #             result.append(combinations.copy())
    #             return 
            
    #         if total_sum >= target or index >= len(candidates):
    #             return 
            
    #         combinations.append(candidates[index])
    #         recursive_func(index, total_sum + candidates[index])
    #         combinations.pop()
    #         recursive_func(index + 1, total_sum)

    #     recursive_func(0, 0)
    #     return result




    #     # res = []
    #     # subset= []
    #     # def Dfs(i, c_sum):
    #     #     if  i >= len(candidates) or c_sum > target:
    #     #         return 

    #     #     if c_sum == target:
    #     #         # if subset.copy() not in res:
    #     #             return res.append(subset.copy())

    #     #     c_sum += candidates[i]
    #     #     subset.append(candidates[i])
    #     #     Dfs(i, c_sum)


    #     #     c_sum -= candidates[i]
    #     #     subset.pop()
    #     #     Dfs(i + 1, c_sum)

    #     # Dfs(0, 0)
    #     # return res































    # # def dfs(self, i, subset, res, nums, target):

        

















    # # #     if sum(subset) == target:
    # # #         res.append(subset.copy())
    # # #         return 
    # # #     if  i >= len(nums) or sum(subset) > target:
    # # #         return

    
    # #     subset.append(nums[i])
    # #     Solution.dfs(self, i, subset, res, nums, target)
        
    # #     subset.pop()
    # #     Solution.dfs(self, i+1, subset, res, nums, target)



    # # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # #     subset = []
    # #     res = []
    # #     Solution.dfs(self, 0, subset, res, candidates, target)
    # #     return res


        
        
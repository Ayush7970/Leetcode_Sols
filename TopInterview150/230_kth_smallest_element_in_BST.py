# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        """
        Practic 1. Good solution but space complexity would be O(n) since you are using array and also the time complexity will also O(n) everytime since you will always loop the whole tree. Better solution is to keep a counter
        """

        # modified code here 
        counter = [0]
        ans = [float("inf")]
        def dfs(root, counter):
            if root == None:
                return 
    
            dfs(root.left, counter)
            counter[0] += 1
            if counter[0] == k:
                ans[0] = root.val
            dfs(root.right, counter)

        dfs(root, counter)
        return ans[0]


        
        





    # def check(self, root, k,  counter, answer):

#         if not root:
#             return 
        
#         Solution.check(self, root.left, k, counter, answer)
#         counter[0] += 1
#         if k == counter[0]:
#             answer[0] = root.val
#             return 
#         Solution.check(self, root.right, k , counter, answer)

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         answer = [float("inf")]
#         counter = [0]
#         Solution.check(self, root, k, counter, answer)
#         return answer[0]
        


# # class Solution:
# #     def inorder_recursive(self, root, k, counter, answer):
# #         if root == None:
# #             return 
        
# #         Solution.inorder_recursive(self, root.left, k, counter, answer)
# #         counter[0] +=  1
# #         if k == counter[0]:
# #             answer[0] = root.val
# #             return  
# #         Solution.inorder_recursive(self, root.right, k, counter, answer)

# #     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# #         answer = [float('inf')]
# #         counter = [0]
# #         Solution.inorder_recursive(self, root, k, counter, answer)
# #         return answer[0]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check (self, root, min_limit, max_limit):
        if root is None:
            return True
        
        if root.val >= max_limit or root.val <= min_limit:
            return False
        return Solution.check(self, root.left, min_limit, root.val) and Solution.check(self, root.right, root.val, max_limit)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.check(self, root, float("-inf"), float("inf"))
        





#class Solution:
#     def check(self, root, max_limit, min_limit):
#         if root == None:
#             return True
#         if root.val >= max_limit or root.val <= min_limit:
#             return False
#         return Solution.check(self, root.left, root.val, min_limit) and Solution.check(self, root.right, max_limit, root.val)

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return Solution.check(self, root, float('inf'), float('-inf'))
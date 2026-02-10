from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        """
        Simple binary Tree question. 
        """

        if not root or (not root.left and not root.right):
            return root.val


        def dfs(root, curr_sum):
            if root.left == None and root.right == None:
                
                return int(curr_sum + str(root.val))

            total_sum = 0
            if root.left:
                total_sum += dfs(root.left, curr_sum + str(root.val))
            if root.right:
                total_sum += dfs(root.right, curr_sum + str(root.val))

            return total_sum


        return dfs(root, "")
        
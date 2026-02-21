# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    """
    Simple Easy question. Recusively traverse the tree and check each node value, with its mirror value.
    T.C -> O(h)
    S.C -> O(h)
    """

    def check(self, l, r):

        return (not l and not r) if (not l or not r) else (l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.check(root.left, root.right)



# class Solution:
#     def checksymmetric(self, L, R):
#         if L == None or R == None:
#             return L == R
        
#         if L.val != R.val:
#             return False
#         return Solution.checksymmetric(self, L.left, R.right) and Solution.checksymmetric(self, L.right, R.left)
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return root == None or Solution.checksymmetric(self, root.left, root.right)
        
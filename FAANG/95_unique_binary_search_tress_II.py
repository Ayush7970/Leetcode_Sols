

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        dp = {}
        def dfs(left, right):

            """
            Try Again
            Really good question. The question was about generating all the binaries tree. In this case we should remeber that one root can have multiple different binary trees on the left and right. That's why we multiple every left_tree with right tree and for all the nodes. 
            The three for loops we ask to return a list for every sub tree, so we exactly divide the problem, into smaller problem, which is what dynamic programming is all about. 
            T.C -> 4^n/n^(3/2)      (Catalan number)
            S.C -> cn * n
            """

            # if left == right:
            #     print(left, "left")
            #     return [TreeNode(left)]
            
            if left > right:
                return [None]

            if (left, right) in dp:
                return dp[(left, right)]

            res = []
            for root in range(left, right + 1):
                for left_tree in dfs(left, root - 1):
                    for right_tree in dfs(root + 1, right):
                        print("For node", root)
                        print("left_tree", left_tree)
                        print(" ")
                        print("right_tree", right_tree)
                        node = TreeNode(root, left_tree, right_tree)
                        res.append(node)
                        print(" ")
                        print( "res", res)
            dp[(left, right)] = res
            return res
                

        return dfs(1, n)
        

        
        
        
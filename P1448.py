# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # think about if you can solve it with bfs or nor for fun 
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        visited = set()
        def dfs(root, max_node, count):

            if root is None:
                return None
            if root.val >= max_node.val:
                count[0] += 1
                max_node = root
            dfs(root.left, max_node, count)
            dfs(root.right, max_node, count)
            return count
        ans = dfs(root, root, count)
        return ans[0]





        # count = [0]
        # visited = set()

        # def dfs(node, max_node, count):
        

        #     if not node:
        #         return 
        #     # print("after if", node.val)
        #     if node not in visited:
        #         visited.add(node)
        #         if node.val >= max_node.val:
        #             print(node.val)
        #             count[0] += 1
        #             max_node = node
        
        #     dfs(node.left, max_node, count)
        #     dfs(node.right, max_node, count)
        #     return count

        # res = dfs(root, root, count)
        # return res[0]



        

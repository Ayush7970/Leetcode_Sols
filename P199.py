# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        answer = []
        level = []
        q = deque([root])
        while len(q) != 0:
            size= len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            answer.extend(level)
        return answer
            








        
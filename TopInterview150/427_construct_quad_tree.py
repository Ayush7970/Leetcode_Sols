"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:

    def check(i, j, limit, grid):

        for x in range(i, i + limit + 1):
            for y in range(j, j + limit + 1):
                if grid[x][y] != grid[i][j]:
                    return False
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':

        """
        Pretty god question. It was matrix and divide and Conquer. It was all about matrix and recursion. Understanding the question was had not implementing it, you just have to understand the indices and hwo the loop works in all the four smaller squares of the matrix.
        """


        def divide(i, j, limit):

            if Solution.check(i, j, limit, grid):
                return Node(grid[i][j], True)
            else:
                root = Node(False, False)
            

                root.topLeft = divide(i, j, limit // 2)
                # print("topLeft")
                root.topRight = divide(i, j + limit // 2 + 1, limit // 2)
                # print("topRight")
                root.bottomLeft = divide(i + limit // 2 + 1, j, limit // 2)
                # print("bottomLeft")
                root.bottomRight = divide(i + limit // 2 + 1, j + limit // 2  + 1, limit // 2)
                # print("bottomRight")

                return root


        return divide(0, 0, len(grid) - 1)


        
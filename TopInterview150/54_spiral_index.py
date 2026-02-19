class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        """
        Matrix Proctice 1 done, Matrix and Array quesition. You just have to create a formula such that it does the spiral. Obiviously you have to use four for loops inside while.
        """


        bottom = len(matrix)
        right = len(matrix[0])
        top, left = 0, 0
        res = []

        while left < right and top < bottom:

            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            if bottom <= top or right <= left:
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res

        









        
        # # rows = len(matrix)
        # # col = len(matrix[0])
        # # top = 0
        # # bottom = rows - 1
        # # left = 0
        # # right = col - 1
        # # ans = []

        # # while bottom >= top and right >= left:
            
        # #     for i in range(left, right+1):
        # #         ans.append(matrix[top][i])
        # #     top = top + 1
            
        # #     for i in range(top, bottom+1):
        # #         ans.append(matrix[i][right])
        # #     right = right - 1
        # #     if not (bottom >= top and right >= left):
        # #         break
        # #     for i in range(right, left-1, -1):
        # #         ans.append(matrix[bottom][i])
        # #     bottom = bottom - 1

                
        # #     for i in range(bottom, top-1, -1):
        # #         ans.append(matrix[i][left])
        # #     left = left + 1
            
            
        # # return ans
        


        
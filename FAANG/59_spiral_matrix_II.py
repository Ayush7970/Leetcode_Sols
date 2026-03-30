
from ast import List



class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        """
        Matrix question Type. Since I have solved the one I remeber the trick that we ahve to create four pointer left,right, top and down. Therefore, it was easy to solve, first we solve the outer square then we solve the inner square by reducing the dimensions. num is the number that fills the value
        T.C -> O(n^2)
        S.C -> O(n^2)
        """


        ans = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, down = 0, n - 1
        num = 1
        while left <= right and top <= down:

            for i in range(left, right + 1):
                ans[top][i] = num
                num += 1
            
            for i in range(top + 1, down):
                ans[i][right] = num
                num += 1

            for i in range(right, left, -1):
                ans[down][i] = num
                num += 1
            
            for i in range(down, top, -1):
                ans[i][left] = num
                num += 1
            
            left += 1
            right -= 1
            top += 1
            down -= 1
        
        return ans
            




        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        top, down = 0, len(matrix) - 1
        COLS = len(matrix[0])

        while top <= down:
            row = (top + down) // 2
            if target < matrix[row][0]:
                down = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
            
        if not (top <= down):
            return False
        
        row = (top + down) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False






        

        # m = len(matrix)
        # n = len(matrix[0])
        # low = 0
        # high = (m * n) - 1
        # while low <= high:
        #     mid = (low + high) // 2
        #     row = mid // n
        #     col = mid % n
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return False


        
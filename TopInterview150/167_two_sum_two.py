class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        Practice 1, I solved it with binary search inside the for loop which is O(n), but there is a better approach which is two pointer, in which you simply start two pointers from two end and if the value is smaller i moves if bigger j moves.
        """


        # for k in range(len(numbers)):
        #     num = target - numbers[k]
        #     i, j = k + 1, len(numbers) - 1
        #     while i <= j:
        #         mid = (i + j) // 2
        #         if numbers[mid] == num:
        #             return [k + 1, mid + 1]
        #         elif numbers[mid] > num:
        #             j = mid - 1
        #         else:
        #             i = mid + 1

        l, r = 0, len(numbers) - 1
        while l < r:
            if target < numbers[l] + numbers[r]:
                r -= 1
            elif target > numbers[l] + numbers[r]:
                l += 1
            else:
                return [l + 1, r + 1]






        # """
        # This is a simple two pointer problem in which you are basically looping from the left pointer and the right pointer and you move left if the target is greater and move right if the target is smaller. 
        # """

        # l = 0
        # r = len(numbers) - 1
        # while l < r:

        #     if target < numbers[l] + numbers[r]:
        #         r -= 1
        #     elif target > numbers[l] + numbers[r]:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        




















        # # i = 0
        # # j = len(numbers) - 1

        # # while i < j:
        # #     sum1 = numbers[i] + numbers[j]
        # #     if target == sum1:
        # #         return [i+1,j+1]
        # #     elif sum1 < target:
        # #         i += 1
        # #     else:
        # #         j -= 1
        # # return []
        
        
class Solution:
    def trap(self, height: List[int]) -> int:

        """
        Simple two pointers from opposite side. You loop and store the max wall and subtract from the amx value to the current value for both of them. From i and j you move teh one which is small so that the other pointers stops at the greatest wall and this the other pointers comes to it instead of the tallest one moving forward, because if you move the tallest it will caculate the water from its length but you dont know what is the height on the other side, it will definately be smaller.
        """


        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        res = 0

        while left < right:

            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]  # this is one of the most important line which basically stores everything which is shorter than the max height, it can never be negative since above we calculate the max_left with these two variable itself.
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]

        return res











        # left =  0
        # right = len(height) - 1
        # maxleft = height[left]
        # maxright = height[right]
        # res = 0
        # while left < right:
            
        #     if maxleft < maxright:
        #         left += 1
        #         maxleft = max(maxleft, height[left])
        #         res += maxleft - height[left]
        #     else:
        #         right -= 1
        #         maxright = max(maxright, height[right])
        #         res += maxright - height[right]
        #     print(left, right, res)
        # return res
















        # # l = 0 
        # # r = len(height) - 1
        # # maxleft = height[l]
        # # maxright = height[r]
        # # res = 0

        # # while l < r:
            
        # #     if maxleft <= maxright:
        # #         l += 1
        # #         maxleft = max(maxleft, height[l])
        # #         res += maxleft - height[l]
        # #     else:
        # #         r -= 1
        # #         maxright = max(maxright, height[r])
        # #         res += maxright - height[r]
        # # return res






        
from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        """
        This question was Bitwise Operation. I could not figure out on my own. But the intuition should come from that they want the answer in O(n) T.C and O(1) S.C and there is no data structure that can store the answer for them O(1) time complexity. Therefore, this should be the first intuition for bitwise operation.

        We basically first check the total number of 1 bit at any position. This was we know that if our numbers bit was present over and was 1 that will not be divible by 3. So we first calculate the number of all bits in one position and if it is not divible by 3 we add 1 at that bit place.
        """

        ans = 0
        for bit in range(32):

            count = 0
            for i in range(len(nums)):
                if nums[i] & (1 << bit):
                    count += 1
                
            if count % 3 != 0:
                ans = ans | (1 << bit)
        
        # convert 32-bit two's complement to Python int if sign bit is set
        if ans >= 1 << 31:
            ans -= 1 << 32

        return ans



        

        
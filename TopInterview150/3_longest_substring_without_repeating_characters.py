class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        practice1
        T.C -> O(2n)
        S.C -> O(n)
        """

        set1 = set()
        max_len = 0
        j = 0
        for i in range(len(s)):
            
            while s[i] in set1:
                set1.remove(s[j])
                j += 1
            max_len = max(max_len, i - j + 1)
            set1.add(s[i])
        
        return max_len
    

    #     """
    #     Thi is also a variable sliding window problem, in which we are simply moving forward by the left pointer when the char is in the set and will be duplcate. However, the only difference in this is that the while loop has the condition which we dont want to happen therefore, we calculate the length after the while loop instead of inside the while loop.
    #     """

    #     result = ""
    #     unique_set = set()
    #     longest_len = 0
    #     left = 0
    #     for i in range(len(s)):
    #         ch = s[i]
    #         while ch in unique_set:

    #             unique_set.remove(s[left])
    #             left += 1
            
    #         longest_len = max(longest_len, i - left + 1) # calculating the length afterwards as it will calculate always after moving one step ahead where it will fidn duplication if we do it inside the while loop 

            

    #         unique_set.add(ch)
    #     return longest_len 




















    #     # set1 = set()
    #     # max_len = 0
    #     # j = 0
    #     # for i in range(len(s)):
    #     #     while s[i] in set1:
    #     #         set1.remove(s[j])
    #     #         j += 1
    #     #     set1.add(s[i])
    #     #     max_len = max(max_len, i - j + 1)
    #     # return max_len

            
            





















        # l = 0
        # res = 0
        # visited = set()
        # for r in range(len(s)):
        #     while s[r] in visited:
        #         visited.remove(s[l])
        #         l += 1
        #     visited.add(s[r])
        #     count = r - l + 1  
        #     res = max(res, count)
        # return res
            

        
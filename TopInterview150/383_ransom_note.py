
from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        """
        I just created a dict to solve it. You cant use set since can't store one character twice.
        """

        check = Counter(magazine)

        for ch in ransomNote:
    
            if check[ch] >= 1:
                check[ch] -= 1
            else:
                return False
        return True
        
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        """
        easy hashmap question, can be done with two dicts
        See Chat gpt solution crazy one

        class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return len(words) == len(pattern) and \
               len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


        """

        dp = defaultdict(str)
        arr = s.split(" ")
        visit= set()
        if len(arr) != len(pattern):
            return False

        for i in range(len(pattern)):

            if pattern[i] not in dp and arr[i] not in visit:
                visit.add(arr[i])
                dp[pattern[i]] = arr[i]
            elif dp[pattern[i]] != arr[i]:
                return False
        
        
        return True
                
        
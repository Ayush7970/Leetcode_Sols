class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        """
        Type: Sliding Window Apporach, If took me time to understand the question. But the question is simple you can only have two fruits (subarray of two different elements) and calculate max of it. 
        """

        dict1 = {}
        j = 0
        max_count = 0
        for i in range(len(fruits)):

            if fruits[i] not in dict1:

                while len(dict1) == 2:
                    dict1[fruits[j]] -= 1
                
                    if dict1[fruits[j]] == 0:
                        del dict1[fruits[j]]
                    j += 1
                    
                dict1[fruits[i]] = 1
            else:
                dict1[fruits[i]] += 1
            
            max_count = max(max_count, i - j + 1)
        
        return max_count
    
    
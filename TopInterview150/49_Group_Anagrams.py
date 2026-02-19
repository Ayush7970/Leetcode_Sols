from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Practice 1, Solution below it is hasing question. ALWAYS REMEMBER, word like duh and ill ahve similar ord count, it is also about the fact that which charcaters are in the word. So best is to use a count array and imagine a as 0 indexing and store the count in it. For dictionary you can just convert it to dictionary. 
        """

        sum1 = 0
        res = []
        dict1 = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord('a') - ord(ch)] += 1
            dict1[tuple(count)].append(word)
        
        for key, values in dict1.items():
            res.append(values)
    
        return res









#         """
#         this question is all about hashing u have to find a way not a formula so that you can be aware of the length of the word and and characters in it, the best way is tuple of 26 length since dictionay keys supprt tuples but not set and array 
#         """

#         dict1 = defaultdict(list)    # to create a list at the values of the dictionary 
#         count = [0] * 26 # this is main trick of the question, we can store a tuple at the list's key but not a set or a list
#         for word in strs:
#             count = [0] * 26
#             for ch in word:
#                 count[ord('a') - ord(ch)] += 1
#             dict1[tuple(count)].append(word)
#         print(dict1)

#         return list(dict1.values())


        











# # from collections import defaultdict
# # class Solution:

# #     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# #         dict1 = defaultdict(list)

# #         for word in strs:
# #             count = [0] * 26
# #             for ch in word:
# #                 count[ord('a') - ord(ch)] += 1
# #             dict1[tuple(count)].append(word)

# #         return list(dict1.values())

            
























#         # map1 = defaultdict(list)
#         # for i in range(len(strs)):
#         #     count = [0] * 26
#         #     for c in strs[i]:
#         #         count[ord(c)- ord("a")] += 1
#         #     map1[tuple(count)].append(strs[i])
#         # return map1.values()


        
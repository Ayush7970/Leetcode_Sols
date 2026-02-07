from collections import defaultdict, Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        """
        Very Head question. Try Again.
        It is a sliding window question in which we are looping through three iteration of sliding window. Then we preform the sliding window with multiple edge cases
        """

 
        ans = []
        word_count = Counter(words)
        n = len(s)
        k = len(words)
        word_len = len(words[0])



        def sliding_window(i):

            words_found = defaultdict(int)
            count = 0
            excess_word = False
            
            left = i
            for right in range(i, n - word_len + 1, word_len):
                if right + word_len > n:
                    break

                sub = s[right : right + word_len]
                if sub not in word_count:
                    words_found = defaultdict(int)
                    count = 0
                    excess_word = False
                    left = right + word_len

                else:
                    
                    while right - left == (len(words) * len(words[0])) or excess_word:

                        leftmost_word = s[left : left + word_len]

                        left += word_len
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            excess_word = False
                        else:
                            count -= 1
                        
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        count += 1
                    else:
                        excess_word = True
                    
                    if count == k and not excess_word:
                        ans.append(left)


        for i in range(len(words[0])):
            sliding_window(i)
        
        return ans
        
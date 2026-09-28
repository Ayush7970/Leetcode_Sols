class Solution:
    def maxSubarray(self, nums: List[int]) -> int:

        """
        In this question we have to calculate the amx subarray, so its variable sliding window problem, i kindof solved the problem, the only area I failed was time complexity of checking the subarray, I was checking all the elements in each subarray that is O(n^2). However, the correct solution is when u add new element x then you only have to check if any two numbers alread yin subarray ewuals to x, a + b = x and then second condition to check if a + x = b. so basically a one combined with x equals to number already present. 

        Missing insught from chatgpt: Whenever you see something like:
value <= 500
value <= 1000
letters = 26
digits = 10

your brain should ask:
Can I scan the entire value domain instead of scanning the whole array?
        """
                
        freq = [0] * 501
        left  = 0
        answer = 0

        def check_bad_triplets(x):
            # case 1
            #a + b = x
            
            for a in range(1, x):
                b = x - a


                if a == b:
                    if freq[a] >= 2:
                        return True
                else:
                    if freq[a] >= 1 and freq[b] >= 1:
                        return True


            # case 2 a = x + b

            for a in range(1, 501):

                b = x + a

                if b > 500:
                    break

                if freq[a] >= 1 and freq[b] >= 1:
                    return True
                
            return False

            
        for right in range(len(nums)):
            
            while check_bad_triplets(nums[right]):
                freq[nums[left]] -= 1
                left += 1

            freq[nums[right]] += 1

            answer = max(answer, right - left + 1)

        return answer

            
                
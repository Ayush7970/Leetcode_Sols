class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:

        """
        This question was a competitive question of dictionaries, the correct solution was you have to think it in a different way of solution, if all the pairs are present what all you need to change to get the max count, there are two kinds of pair, a == b, we dont care about coz this will always be true, but a != b, we can store their frequency in the dictionary, and the highest frequency pair is the correct answer.
        T.C -> O(n)
        S.C -> O(n)
        """

        equal_pairs = 0
        count_dict = defaultdict(int)
        max_unequal_pair_count = 0
        for a, b in zip(nums, nums[1:]):

            if a == b:
                equal_pairs += 1
            else:
                pair = (min(a, b), max(a, b))
                count_dict[pair] += 1
                max_unequal_pair_count = max(max_unequal_pair_count, count_dict[pair])
        print(equal_pairs, max_unequal_pair_count)
        return equal_pairs + max_unequal_pair_count
                
                



                    
                
            
            
        
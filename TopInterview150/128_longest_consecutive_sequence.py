
class UnionFind:
    
    """
    There are two good solutios for this question:
    1. Graph type Union Find -> In this approach you are using union by size that means you will add the size of the other tree  everytime instead of just adding one to the rank. when they are equal. In our solution you will return the size, as it is calculating the longest consecutive sequence for us. Then the difficult part was also to realize that you have to enumerate the nums and use an dictionary with elem to index, as it will help us to check if elem - 1 or elem + 1 exist in our array. if it exist and we already checked then we return the same size (which is false in union by rank). 
    T.C for looping through dict O(n) and then O(alpha * n) => O(1) to O(n)

    2. This is another perfect apporach of T.C -> O(n). In this you create a set and store all the elements in the set. Then you start looping through the set (to prevent duplicates (not the array)) (This saves computation by O(n) in workst case, as you will not recalcualte for same number in while loop, (you could have also used a visited set)) and you check if there is an element 1 less thant he current element exist or not. If not it start calcuting the +1 element exist or not in a while loop. This way whenver we will find the minimum element, it will keep on looping through the whole consecutvie sequence and return the length of it. 
    """
    def __init__(self, length):
        self.par = [i for i in range(length)]
        self.size = [1 for i in range(length)]
    
    def find(self, x):

        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return self.size[p2]


        if self.size[p1] < self.size[p2]:
            p1, p2, = p2, p1
        
        self.par[p2] = p1
        self.size[p1] += self.size[p2]
        return self.size[p1]

    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        uf = UnionFind(n) 
        pos = {}
        best = 1
        for ind, value in enumerate(nums):

            if value in pos:
                continue      # removing duplicates
            
            pos[value] = ind


            if value - 1 in pos:
                best = max(best, uf.union(ind, pos[value - 1]))
            if value + 1 in pos:
                best = max(best, uf.union(ind, pos[value + 1]))
        
        return best

        set1 = set(nums)

        max1 = 0
        for i in set1:

            if i - 1 not in set1:
                count = 1
                x = i
                while x + 1 in set1:
                    count += 1
                    x += 1
                max1 = max(max1, count)
        return max1

        # # set_1 = set(nums)
        # # max_count = 0
        # # for i in range(len(nums)):

        # #     if nums[i] - 1 not in set_1:
        # #         count = 1
        # #         x = nums[i]
        # #         while (x + 1) in set_1:
        # #             count += 1
        # #             x = x + 1
        # #         max_count = max(count, max_count)
        # # return max_count

        # # n = len(nums)
        # # if n == 0:
        # #     return 0
        # # longest = 1
        # # set1 = set()
        # # for i in range(n):
        # #     set1.add(nums[i])

        # # for j in set1:
        # #     if j - 1 not in set1:
        # #         count = 1
        # #         x = j
        # #         while x + 1 in set1:
        # #             count = count + 1
        # #             x = x + 1
        # #         longest = max(longest, count)
        # # return longest

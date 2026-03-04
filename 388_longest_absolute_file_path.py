class Solution:
    def lengthLongestPath(self, input: str) -> int:

        """
        Good question: Type: Stack and DFS. It was more about how you will identify the level and handle it accoridngly. That is what oyu have to learn.

        In this specifc question, we first loop through the array by splitting through n. Then we first identify the level with the hel pof counting \t. Then w count the length and the add the previous. Then if it a file we store the max, otherwise we update it in the path dict. The important and smart thing is every file will come just after its directory, so we can always just update the leng th of the sub_dir, basically level and dont have to worry about mismatch of level and dir.
        """

        chunks = input.split('\n')
        path = {}
        max_len = 0
        for c in chunks:
            
            level = 0
            while level < len(c) and c[level] == "\t":
                level += 1

            if level == 0:
                path_len = len(c)
            else:
                path_len = path[level - 1] + 1 + len(c[level:])
            
            if '.' in c:
                max_len = max(max_len, path_len)
            else:
                path[level] = path_len
            
        return max_len

        
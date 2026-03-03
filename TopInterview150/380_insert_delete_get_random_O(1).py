class RandomizedSet:

    """
    Great question of DSA and Array.

    Insert -> you simply ahve to add to the lsit and beofre adding it to the list youy ahv eto add to map, The important part is what is the index. The index should be the lengrh of the array before adding element to the array len(arr) - 1 after adding 

    Delete-> you cna check the list if element exist or not. If it exist you ge the index from the list and IMPORTANTLY you store the value of the last element in list1 where the element to be deleted exist (since you know the index) this way oyu can just pop the list1 now and you will be deleting in O (1). Remember to update the index in the hashmap, of the value you switched to new place from the end of array.
    """

    def __init__(self):
        self.hash_map = {}
        self.list1 = []
        

    def insert(self, val: int) -> bool:

        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.list1)
        self.list1.append(val)
        return True
        

    def remove(self, val: int) -> bool:

        if val in self.hash_map:
            index = self.hash_map[val]
            last_value = self.list1[-1]
            self.list1[index] = last_value
            self.list1.pop()
            self.hash_map[last_value] = index
            del self.hash_map[val]
            return True
        return False

    def getRandom(self) -> int:

        return random.choice(self.list1)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()





# class RandomizedSet:

#     def __init__(self):
#         self.hashmap = {}
#         self.list1 = []
        
#     def insert(self, val: int) -> bool:
#         res = val not in self.hashmap
#         if res:
#             self.hashmap[val] = len(self.list1)
#             self.list1.append(val)
#         return res

#     def remove(self, val: int) -> bool:
#         res = val in self.hashmap
#         if res:
#             idx = self.hashmap[val]
#             last_val = self.list1[-1]
#             self.list1[idx] = last_val
#             self.list1.pop()
#             self.hashmap[last_val] = idx
#             del self.hashmap[val]
#         return res
#     def getRandom(self) -> int:
#         return random.choice(self.list1)
        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()
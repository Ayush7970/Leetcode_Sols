class MinStack:

    """
    This a stact style: Invariant / Encoding Tricks
    this is a encoded = (2 * val) - prev_min_val, which can be retrieved by 2 * val - encoded 
    This is important to understand. since in every question you should understnd what is the information that is missing and how can we encode it. Remember this, if you wanna be the best.
    """

    def __init__(self):
        self.stack = []
        self.min_value = float("-inf")
    

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_value = val
        else:
            if val < self.min_value:
                self.stack.append(2 * val - self.min_value) # this will always be greater than val since more than will be cut off when we subtract min_value
                self.min_value = val
            else:
                self.stack.append(val)

    def pop(self) -> None:

        if len(self.stack) == 1:
            self.min_value = float("-inf")
            return self.stack.pop()
        else:
            if self.min_value > self.stack[-1]:
                self.min_value = 2 * self.min_value - self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 
        element = self.stack[-1]
        if element < self.min_value:
            return self.min_value
        return element

        

    def getMin(self) -> int:
        return self.min_value
        




# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()



# # class MinStack:

# #     def __init__(self):
# #         self.stack1 = []
# #         self.min_elem = float('inf')

# #     def push(self, val: int) -> None:
        
# #         if len(self.stack1) == 0:
# #             self.stack1.append(val)
# #             self.min_elem = val
# #         else:
# #             if self.min_elem > val:
# #                 self.stack1.append(2 * val - self.min_elem)
# #                 self.min_elem = val
# #             else:
# #                 self.stack1.append(val)

# #     def pop(self) -> None:
# #         if len(self.stack1) == 0:
# #             return
# #         else:
# #             el = self.stack1[-1]
# #             if el < self.min_elem:
# #                 self.min_elem = 2 * self.min_elem - el
# #             self.stack1.pop()

# #     def top(self) -> int:
# #         if len(self.stack1) == 0:
# #             return
# #         else:
# #             el = self.stack1[-1]
# #             if el < self.min_elem:
# #                 return self.min_elem
# #             return el

# #     def getMin(self) -> int:
# #         # if len(self.stack1) == 0:
# #         #     self.min_elem = -1
# #         return self.min_elem
        
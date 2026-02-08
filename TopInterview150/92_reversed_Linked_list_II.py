# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode, Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)


        prev = dummy
        for i in range(1, left):
            prev = prev.next

        
        curr = prev.next
        for _ in range(right - left):
            node = curr
            curr = curr.next
            node.next = prev
            prev = node

        return dummy.next



        





# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverse_func(head):

#         curr = head
#         prev = None
#         while curr != None:
#             node = curr
#             curr = curr.next
#             node.next = prev
#             prev = node
#         return prev


#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

#         if not head or not head.next or left == right:
#             return head

#         dummy = ListNode(-1)

#         dummy.next = head
#         curr = head
#         entry = None 
#         end = None
#         i = 1
#         while curr != None:

#             if i == left - 1:
#                 entry = curr
#             if i == right:
#                 end = curr

#             i += 1
#             curr = curr.next


#         if end:
#             after = end.next
#             end.next = None

#         if not entry:
#             entry = dummy
#         reverse_head = Solution.reverse_func(entry.next)
#         entry.next = reverse_head

#         curr2 = reverse_head

#         while curr2.next != None:
#             curr2 = curr2.next
        
#         curr2.next = after 

#         return dummy.next
        

        
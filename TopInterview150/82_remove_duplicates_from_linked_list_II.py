from collections import defaultdict
from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Linked list question. For these you dont need to identify topics genrally, its simple since topic is Linked List. One important thing is to generally create a DummyNode to prevent edge case on First node.
        """

        dp = defaultdict(int)
        curr = head
        while curr != None:
            dp[curr.val] += 1

            curr = curr.next

        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        while curr != None:
    
            if dp[curr.val] > 1:
                curr = curr.next
                prev.next = prev.next.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            
        """
        Good Linked List Question. Solved in 27 mins 30 sec.
        """

        dummy = ListNode(-1, head)

        curr = dummy.next
        prev = dummy
        feed = None
        feed_prev = None
        cond = True
        while curr != None:

            if curr.val >= x and cond:
                cond = False
                feed = curr
                feed_prev = prev
            
            if curr.val < x and feed != None:
                prev.next = prev.next.next
                next_node = curr.next
                curr.next = feed
                feed_prev.next = curr
                feed_prev = curr
                curr = next_node
            else:
                prev = curr
                curr = curr.next

        
        return dummy.next

        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        Simple Linked lsit question. The optimized approach is not to loop k time instead % it with the length so that you can get where to break the linked list and then just solve the question.
        """

        if not head or not head.next:
            return head
        curr = head
        length = 0
        tail = None
        while curr != None:
            length += 1
            tail = curr
            curr = curr.next

        loop = length - (k % length)

        curr = head
        count = 0
        prev = None
        if loop == 0 or loop == length:
            return head
            
        while curr != None:
            count += 1
            if count == loop:
                newhead = curr.next
                curr.next = None
                tail.next = head
                return newhead
            curr = curr.next
        
        return None


        
        
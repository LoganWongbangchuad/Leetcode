# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        dummy = ListNode(0) 
        current = dummy
        for val in reversed(values):
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next

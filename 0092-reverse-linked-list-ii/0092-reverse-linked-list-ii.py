# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # 1. Use a dummy node to easily handle cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        
        # Move 'before_sublist' to the node right before the reversal zone
        before_sublist = dummy
        for _ in range(left - 1):
            before_sublist = before_sublist.next
            
        # 2. Perform a standard linked list reversal on the sub-list
        prev = None
        curr = before_sublist.next  # This will become the tail of the reversed sub-list
        
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 3. Reconnect the pieces back together
        # before_sublist.next still points to the old sub-list start (which is now the tail)
        # We point its next to 'curr' (the node right after the reversal zone)
        before_sublist.next.next = curr
        
        # Point 'before_sublist' to 'prev' (the new head of the reversed sub-list)
        before_sublist.next = prev
        
        return dummy.next
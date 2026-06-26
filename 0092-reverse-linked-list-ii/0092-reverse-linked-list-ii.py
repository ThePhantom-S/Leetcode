# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Use a dummy node to seamlessly handle cases where 'left' is the head (1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Move 'prev' to the node right before the sub-list starts
        for _ in range(left - 1):
            prev = prev.next
            
        # 'current' will point to the start of the sub-list to be reversed
        current = prev.next
        
        # Step 2: Reverse the sub-list using a single pass (hooking nodes forward)
        for _ in range(right - left):
            forward = current.next
            current.next = forward.next
            forward.next = prev.next
            prev.next = forward
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits1, digits2 = [], []
        while l1:
            digits1.append(l1.val)
            l1 = l1.next
        while l2:
            digits2.append(l2.val)
            l2 = l2.next

        # Add using buffer
        carry = 0
        res_digits = []
        n1, n2 = len(digits1), len(digits2)
        for i in range(max(n1, n2)):
            v1 = digits1[i] if i < n1 else 0
            v2 = digits2[i] if i < n2 else 0
            carry, digit = divmod(v1 + v2 + carry, 10)
            res_digits.append(digit)
        if carry:
            res_digits.append(carry)

        # Build linked list from result buffer
        dummy = curr = ListNode()
        for d in res_digits:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            if total <= 9:
                curr.next = ListNode(total)
            else:
                digit = total % 10
                curr.next = ListNode(digit)
            carry = total // 10
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        while l1:
            total = carry + l1.val
            if total <= 9:
                curr.next = ListNode(total)
            else:
                digit = total % 10
                curr.next = ListNode(digit)
            carry = total // 10
            l1 = l1.next
        while l2:
            total = carry + l2.val
            if total <= 9:
                curr.next = ListNode(total)
            else:
                digit = total % 10
            carry = total // 10
            l2 = l2.next
        if carry: curr.next = ListNode(carry)
        
        return dummy.next

        
